import json
import os
from typing import List, Any, Dict, Tuple

from BaseClasses import Region, Tutorial, ItemClassification, LocationProgressType, \
    MultiWorld
from worlds.AutoWorld import WebWorld, World
from worlds.Files import APPlayerContainer
from worlds.generic.Rules import add_item_rule
from worlds.LauncherComponents import launch_subprocess, components, Component, Type

from .Items import LRFF13Item, item_data_table, item_table, filler_items, filler_weights
from .Locations import LRFF13Location, location_data_table, location_table
from .Options import LRFF13GameOptions
from .Regions import region_data_table
from .Rules import location_rule_data_table, entrance_rule_data_table, item_rule_data_table
from .Events import event_data_table
from rule_builder import rules


class LRFF13Container(APPlayerContainer):
    """AP container for LRFF13 output, carrying mod JSON payload inside."""
    game: str = "Lightning Returns: Final Fantasy XIII"
    patch_file_ending: str = ".aplrff13"

    def __init__(self, *args: Any, data: Dict[str, Any] = None, **kwargs: Any) -> None:
        self.data = data or {}
        super().__init__(*args, **kwargs)

    def write_contents(self, opened_zipfile) -> None:
        # Write the JSON content used by the LR mod tool
        opened_zipfile.writestr("seed.json", json.dumps(self.data))
        # Write the AP manifest last
        super().write_contents(opened_zipfile)


def launch_client(*args):
    from .Client import launch
    launch_subprocess(launch, name="Lightning Returns: Final Fantasy XIII Client", args=args)


components.append(Component("Lightning Returns: Final Fantasy XIII Client", "LRFF13Client",
                            func=launch_client, component_type=Type.CLIENT,
                            game_name="Lightning Returns: Final Fantasy XIII", supports_uri=True))

class LRFF13WebWorld(WebWorld):
    theme = "ocean"

    tutorials = [Tutorial(
    "Multiworld Setup Guide",
    "A guide to playing Lightning Returns: Final Fantasy XIII multiworld.",
        "English",
    "guide_en.md",
    "docs",
        ["Bartz24"]
    )]


class LRFF13World(World):
    """TODO"""

    initial_equipment_location_ids = ("tre_box_p_003", "tre_box_p_200", "tre_box_p_201")

    generation_options = (
        "ultimate_lair",
        "superbosses",
        "canvas_of_prayers",
        "grindy",
        "shuffle_teleport",
        "shuffle_escape",
        "shuffle_chronostasis",
        "shuffle_curaga",
        "shuffle_arise",
        "shuffle_esunada",
        "shuffle_quake",
        "shuffle_decoy",
        "shuffle_army_of_one",
        "allow_dlc_items",
        "fully_remote_items",
    )

    game = "Lightning Returns: Final Fantasy XIII"
    data_version = 3
    web = LRFF13WebWorld()
    options_dataclass = LRFF13GameOptions
    options: LRFF13GameOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    ut_can_gen_without_yaml = True

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.used_items = set()
        self.re_gen_data = {}
        self.origin_region_name = "Initial"
        self.locked_items : Dict[str, str] = {loc_id: None for loc_id in self.initial_equipment_location_ids}
        self.excluded_locations: Dict[str, tuple[str, int]] = {}
        self.shop_materials: Dict[str, List[str]] = {}

    def create_item(self, name: str) -> LRFF13Item:
        return LRFF13Item(name, item_data_table[name].classification, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        self.used_items.clear()
        item_pool: List[LRFF13Item] = []
        # Start with non-adornment progression items
        progression_items = [name for name, data in item_data_table.items()
                             if data.classification & ItemClassification.progression and data.category != "Adornment" and (not "DLC" in data.traits or self.options.allow_dlc_items)]

        all_adornments = [name for name, data in item_data_table.items()
                          if data.classification & ItemClassification.progression and data.category == "Adornment" and (not "DLC" in data.traits or self.options.allow_dlc_items)]
        
        # Add always in the pool adornments
        always_adornments = [name for name in all_adornments if "Always" in item_data_table[name].traits]
        progression_items.extend(always_adornments)

        non_always_adornments = [name for name in all_adornments if name not in always_adornments]

        # Add 70-100 adornments total (including always in pool)
        other_count = self.multiworld.random.randint(70 - len(always_adornments), 100 - len(always_adornments))
        other_adornments = self.multiworld.random.sample(non_always_adornments, other_count)
        progression_items.extend(other_adornments)

        for name in progression_items:
            for _ in range(item_data_table[name].duplicate_amount):
                item_pool.append(self.create_item(name))                

        # Get count of non event locations
        non_events = len([location for location in self.multiworld.get_locations(self.player)
                          if location.name not in event_data_table.keys()])

        # Start with non-equipment useful items
        useful_items = [name for name, data in item_data_table.items()
                        if data.classification & ItemClassification.useful and
                        data.category not in ["Garb", "Weapon", "Shield", "Accessory"] and
                        (not "DLC" in data.traits or self.options.allow_dlc_items)]

        # Add equipment to fill up half of the remaining pool
        all_equipment_items = [name for name, data in item_data_table.items()
                           if data.classification == ItemClassification.filler and
                           data.category in ["Garb", "Weapon", "Shield", "Accessory"] and
                           (not "DLC" in data.traits or self.options.allow_dlc_items)]
        
        # Remove initial equipment
        all_equipment_items = [item for item in all_equipment_items if item not in ["Equilibrium", "Dark Muse", "Crimson Blitz", "Scramasax", "Night Lotus", "Double Cross"]]

        # Set locked initial items and remove them from the equipment pool.
        for loc_id, category in zip(self.initial_equipment_location_ids, ("Garb", "Weapon", "Shield")):
            if self.locked_items[loc_id] is None:
                self.locked_items[loc_id] = self.get_initial_and_remove_from_pool(category, all_equipment_items)
            else:
                all_equipment_items.remove(self.locked_items[loc_id])

        def get_remaining_count():
            val = non_events - len(item_pool) - len(self.locked_items)
            # Add back intersection of locked and excluded locations
            locked_locations = set(self.locked_items.keys())
            locked_location_names = {next((name for name, data in location_data_table.items() if data.str_id == loc_str_id), None)
                                     for loc_str_id in locked_locations}
            excluded_locked = locked_location_names.intersection(set(self.excluded_locations.keys()))
            return val + len(excluded_locked)

        selected_count = (get_remaining_count() - len(useful_items)) // 2
        selected_equipment = self.multiworld.random.sample(all_equipment_items, selected_count)
        useful_items.extend(selected_equipment)

        self.add_to_pool(item_pool, useful_items)

        # Remove any locked items from the pool
        item_pool = [item for item in item_pool if item.name not in self.locked_items.values()]

        filler_count = get_remaining_count()  

        # Add filler items to the pool
        for _ in range(filler_count):
            filler = self.get_filler_item_name()
            self.used_items.add(filler)
            item_pool.append(self.create_item(filler))

        # Set excluded location filler items
        for location_name, _ in self.excluded_locations.items():
            filler = self.get_filler_item_name(location_name)
            self.used_items.add(filler)

            item_name = filler
            count = item_data_table[filler].amount
            self.excluded_locations[location_name] = (item_name, count)

        self.multiworld.itempool += item_pool

    def get_initial_and_remove_from_pool(self, category: str, pool : list[str]) -> str:
        possible = [item for item in pool if item_data_table[item].category == category]

        # Ignore ultima weapon, ultima shield, equilibrium+ and mist wizard+
        possible = [item for item in possible if item not in ["Ultima Weapon", "Ultima Shield", "Equilibrium+", "Mist Wizard+"]]

        if len(possible) == 0:
            raise Exception(f"No items of category {category} found in pool to set as initial item.")
        selected = self.multiworld.random.choice(possible)
        pool.remove(selected)
        return selected

    def add_to_pool(self, item_pool, items):
        for name in items:
            self.used_items.add(name)
            for _ in range(item_data_table[name].duplicate_amount):
                item_pool.append(self.create_item(name))

    def create_regions(self) -> None:
        # Create regions
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Add connections
        for region_name, data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_exits(region_data_table[region_name].connecting_regions)

        # Add all locations
        for location_name, loc_data in location_data_table.items():
            # If it's excluded, add it to the excluded locations dictionary with an empty item
            if self.excluded_locations.get(location_name) is not None and not self.options.fully_remote_items:
                continue

            region = self.multiworld.get_region(loc_data.region, self.player)
            region.add_locations({location_name: loc_data.address}, LRFF13Location)
            self.multiworld.get_location(location_name, self.player).progress_type = (
                self.get_loc_classification(location_name))

        # Add events in their respective regions
        for event_name, e_data in event_data_table.items():
            region = self.multiworld.get_region(e_data.region, self.player)
            region.locations.append(LRFF13Location(self.player, event_name, None, region))

        # debug log
        import logging
        logging.debug(f"LRFF13: Created {len(self.multiworld.regions)} regions, "
                      f"{len(self.multiworld.get_locations(self.player))} locations.")

    def get_loc_classification(self, location_name: str) -> LocationProgressType:
        if location_name in self.excluded_locations:
            return LocationProgressType.EXCLUDED

        location_data = location_data_table[location_name]
        return location_data.classification

    def get_filler_item_name(self, location_name: str = None) -> str:
        possible = [f for f in filler_items if (not "DLC" in item_data_table[f].traits or self.options.allow_dlc_items) and item_data_table[f].category not in ["Garb", "Weapon", "Shield", "Accessory"]]

        # If location name starts with tre_qst, disallow recovery items as they can cause infinite loading
        if location_name and location_name.startswith("tre_qst"):
            possible = [f for f in possible if item_data_table[f].category != "Item"]

        possible_weights = [item_data_table[f].weight for f in possible]
        return self.multiworld.random.choices(possible, weights=possible_weights)[0]

    def set_rules(self) -> None:
        # Set location rules
        for location in self.multiworld.get_locations(self.player):
            # Use location rule table if available
            if location.name in location_rule_data_table:
                self.set_rule(location, location_rule_data_table[location.name])

        # Set entrance rules
        for region in self.multiworld.regions:
            if region.player != self.player:
                continue
            for entrance in region.exits:
                entrance_tuple = (entrance.parent_region.name, entrance.connected_region.name)
                if entrance_tuple in entrance_rule_data_table:
                    self.set_rule(entrance, entrance_rule_data_table[entrance_tuple])

        # Set initial equipment locked items
        for loc_str_id, item_name in self.locked_items.items():
            loc_name = next((name for name, data in location_data_table.items() if data.str_id == loc_str_id), None)
            if loc_name is None:
                raise Exception(f"Location with string ID {loc_str_id} not found in location data table.")

            if loc_name in self.excluded_locations:
                continue

            if item_name is None:
                raise Exception(f"Initial item for location {loc_name} was not set properly.")
            location = self.multiworld.get_location(loc_name, self.player)
            location.place_locked_item(self.create_item(item_name))

        # Set event locked items
        for event_name, e_data in event_data_table.items():
            location = self.multiworld.get_location(event_name, self.player)
            location.place_locked_item(self.create_event(e_data.item))

        # Set item rules
        for (location_name, rule) in item_rule_data_table.items():
            location = self.multiworld.get_location(location_name, self.player)
            add_item_rule(location, rule)
            add_item_rule(location, lambda i: i.player == self.player)

        # Add rules to material events for each shop item
        events = [event for event in event_data_table.keys() if event_data_table[event].region == "Shops"]
        for event in events:
            # Find the first trait that starts with mat_z_
            item_id = next((trait for trait in event_data_table[event].traits if trait.startswith("mat_z_")), None)
            if item_id is None:
                raise Exception(f"No material trait found for shop event {event}.")
            
            # Add a OR rule for each shop that sells the material
            shops_with_item = [shop for shop, materials in self.shop_materials.items() if item_id in materials]

            or_rule = rules.Has(shops_with_item[0] + "_Shop")
            for shop in shops_with_item[1:]:
                or_rule = or_rule | rules.Has(shop + "_Shop")
            self.set_rule(self.multiworld.get_location(event, self.player), or_rule)

        # Completion condition.
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_event(self, event_item: str) -> LRFF13Item:
        name = event_item
        return LRFF13Item(name, ItemClassification.progression, None, self.player)

    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        slot_data = re_gen_passthrough.get(self.game, {})
        for key, value in slot_data.get("options", {}).items():
            opt = getattr(self.options, key, None)
            if opt is not None:
                setattr(self.options, key, opt.from_any(value))

        excluded_str_ids = set()
        if not self.options.ultimate_lair:
            for loc_name, loc_data in location_data_table.items():
                if loc_data.region == "Ultimate Lair":
                    excluded_str_ids.add(loc_data.str_id)
        if not self.options.superbosses:
            excluded_str_ids.add("btsc04990") # Aeronite Monster Flesh
            excluded_str_ids.add("tre_acc_a_9210") # Ereshkigal Drop
            excluded_str_ids.add("tre_qst_099") # Ereshkigal Reward
        if not self.options.canvas_of_prayers:
            for loc_name, loc_data in location_data_table.items():
                if loc_data.region in ["CoP Global", "CoP Dead Dunes", "CoP Luxerion", "CoP Wildlands", "CoP Yusnaan"]:
                    excluded_str_ids.add(loc_data.str_id)
        if not self.options.grindy:
            excluded_str_ids.add("tre_seed_1st_01") # 20+ Soul Seeds
            excluded_str_ids.add("tre_seed_1st_02") # 30+ Soul Seeds
            excluded_str_ids.add("tre_seed_1st_03") # 40+ Soul Seeds
            excluded_str_ids.add("tre_seed_1st_04") # 50+ Soul Seeds
            excluded_str_ids.add("tre_key_d_kant3") # 10+ Unappraised
            excluded_str_ids.add("tre_key_d_kant4") # 20+ Unappraised
            excluded_str_ids.add("tre_key_d_kant5") # 50+ Unappraised

        # Add all excluded locations to the dictionary with an empty item
        for loc_name, loc_data in location_data_table.items():
            if loc_data.classification == LocationProgressType.EXCLUDED:
                excluded_str_ids.add(loc_data.str_id)

        self.excluded_locations = {name: ("", 0) for str_id in excluded_str_ids
                                   if (name := next((name for name, data in location_data_table.items()
                                                     if data.str_id == str_id), None)) is not None}
        if None in self.excluded_locations:
            raise Exception("One or more excluded locations could not be found in the location data table.")

        if not self.options.shuffle_teleport:
            self.locked_items["tre_ti810"] = "Teleport"
        if not self.options.shuffle_escape:
            self.locked_items["tre_ti830"] = "Escape"
        if not self.options.shuffle_chronostasis:
            self.locked_items["tre_ti840"] = "Chronostasis"
        if not self.options.shuffle_curaga:
            self.locked_items["tre_ti000"] = "Curaga"
        if not self.options.shuffle_arise:
            self.locked_items["tre_box_p_101"] = "Arise"
        if not self.options.shuffle_esunada:
            self.locked_items["tre_box_p_103"] = "Esunada"
        if not self.options.shuffle_quake:
            self.locked_items["tre_box_p_110"] = "Quake"
        if not self.options.shuffle_decoy:
            self.locked_items["tre_box_p_108"] = "Decoy"
        if not self.options.shuffle_army_of_one:
            self.locked_items["tre_box_p_106"] = "Army of One"

        initial_equipment = slot_data.get("initial_equipment", [])
        if initial_equipment:
            self.locked_items.update(zip(self.initial_equipment_location_ids, initial_equipment))

        shop_ids = ["shop_etc_dd00", "shop_etc_lx00", "shop_etc_lx01", "shop_etc_wl00", "shop_etc_wl01", "shop_etc_wl02", "shop_etc_ys00", "shop_etc_ys01"]

        if "shop_materials" in slot_data:
            self.shop_materials = slot_data["shop_materials"]
            return

        # Randomize shop materials so that there's 8 per material shop (starting with mat_z_)
        valid = False
        while not valid:
            self.shop_materials = {}
            material_items = [item.str_id for item in item_data_table.values() if item.str_id.startswith("mat_z_")]
            for shop_id in shop_ids:
                materials_for_shop = self.multiworld.random.sample(material_items, 8)
                self.shop_materials[shop_id] = materials_for_shop

            # Ensure each material appears in at least one shop
            material_coverage = {material: False for material in material_items}
            for materials in self.shop_materials.values():
                for material in materials:
                    material_coverage[material] = True
            valid = all(covered for covered in material_coverage.values())

        return

    def generate_output(self, output_directory: str) -> None:
        spheres: List[Dict[str, Any]] = []
        cur_sphere = 0
        for locations in self.multiworld.get_spheres():
            for loc in locations:
                if loc.name in location_data_table.keys():
                    spheres.append({"id": location_data_table[loc.name].str_id,
                                    "sphere": cur_sphere})
                elif loc.name in event_data_table.keys():
                    spheres.append({"id": loc.name[:loc.name.index(" Event ")],
                                    "item": event_data_table[loc.name].item,
                                    "sphere": cur_sphere})
            cur_sphere += 1

        # Build item placements for LR mod tool
        item_placements: List[Dict[str, Any]] = []
        for loc in self.multiworld.get_locations(self.player):
            if loc.name in event_data_table:
                continue
            # Only include locations that have an item placed
            if getattr(loc, "item", None) is None:
                continue
            item = loc.item
            src_player_name = self.multiworld.get_player_name(item.player)
            display_name = f"{src_player_name}'s {item.name}"
            item_placements.append({
                "id": location_data_table[loc.name].str_id,
                "name": display_name,
                "region": loc.parent_region.name,
                "address": location_data_table[loc.name].address
            })

        # Build local item placements, starting with the initial equipment checks
        local_item_placements: List[Dict[str, Any]] = []
        initial_equip_loc_ids = ["tre_box_p_003", "tre_box_p_200", "tre_box_p_201"]
        for loc_id in initial_equip_loc_ids:
            loc_name = next((name for name, data in location_data_table.items() if data.str_id == loc_id), None)
            if loc_name is None:
                raise Exception(f"Location with string ID {loc_id} not found in location data table.")
            location = self.multiworld.get_location(loc_name, self.player)
            if getattr(location, "item", None) is None:
                raise Exception(f"Initial equipment location {loc_name} does not have an item placed.")
            item = location.item
            local_item_placements.append({
                "location_id": location_data_table[loc_name].str_id,
                "item_id": item_data_table[item.name].str_id,
                "amount": item_data_table[item.name].amount
            })  
        
        # Add excluded locations with their filler items when AP is not handling them.
        if not self.options.fully_remote_items:
            for loc_name, (item_name, amount) in self.excluded_locations.items():
                if item_name == "" or amount == 0:
                    continue
                local_item_placements.append({
                    "location_id": location_data_table[loc_name].str_id,
                    "item_id": item_data_table[item_name].str_id,
                    "amount": amount
                })

        seed_name = self.multiworld.seed_name + "_" + self.multiworld.get_player_name(self.player)
        data = {
            "seed": seed_name,  # to identify the seed
            "type": "archipelago",  # to identify the seed type
            # Retain archipelago details for debugging/auxiliary tools
            "archipelago": {
                "version": self.world_version.as_simple_string(),
                "used_items": list(self.used_items),
                "spheres": spheres,
                "item_placements": item_placements,
                "local_item_placements": local_item_placements,
                "allow_dlc_items": bool(self.options.allow_dlc_items),
                "fully_remote_items": bool(self.options.fully_remote_items),
                "shop_materials": self.shop_materials
            }
        }
        # Package output using an APPlayerContainer for consistency with other worlds
        mod_name = self.multiworld.get_out_file_name_base(self.player)
        container = LRFF13Container(
            path=os.path.join(output_directory, f"{mod_name}{LRFF13Container.patch_file_ending}"),
            player=self.player,
            player_name=self.multiworld.get_file_safe_player_name(self.player),
            server="",
            data=data,
        )
        container.write()

    def fill_slot_data(self) -> Dict[str, Any]:
        initial_equip = []
        for loc_id in self.initial_equipment_location_ids:
            loc_name = next((name for name, data in location_data_table.items() if data.str_id == loc_id), None)
            if loc_name is None:
                raise Exception(f"Location with string ID {loc_id} not found in location data table.")
            location = self.multiworld.get_location(loc_name, self.player)
            if getattr(location, "item", None) is None:
                raise Exception(f"Initial equipment location {loc_name} does not have an item placed.")
            initial_equip.append(location.item.name)

        return {
            "initial_equipment": initial_equip,
            "options": self.options.as_dict(*self.generation_options),
            "shop_materials": self.shop_materials,
        }

    # From Tunic implementation
    # For the universal tracker, doesn't get called in standard gen
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data
