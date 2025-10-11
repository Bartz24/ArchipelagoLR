import json
import os
from typing import List, Any, Dict

from BaseClasses import Region, Tutorial, ItemClassification, CollectionState, Callable, LocationProgressType, \
    MultiWorld
from worlds.AutoWorld import WebWorld, World
from worlds.Files import APPlayerContainer
from worlds.generic.Rules import add_rule, add_item_rule
from worlds.LauncherComponents import launch_subprocess, components, Component, Type

from .Items import LRFF13Item, item_data_table, item_table, filler_items, filler_weights
from .Locations import LRFF13Location, location_data_table, location_table
from .Options import LRFF13GameOptions
from .Regions import region_data_table
from .Rules import location_rule_data_table, entrance_rule_data_table, item_rule_data_table
from .Events import event_data_table


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

LRFF13_VERSION = "0.1.0"


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

    def create_item(self, name: str) -> LRFF13Item:
        return LRFF13Item(name, item_data_table[name].classification, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        self.used_items.clear()
        item_pool: List[LRFF13Item] = []
        progression_items = [name for name, data in item_data_table.items()
                             if data.classification & ItemClassification.progression]

        for name in progression_items:
            for _ in range(item_data_table[name].duplicate_amount):
                item_pool.append(self.create_item(name))

        other_useful_items = [name for name, data in item_data_table.items()
                              if data.classification & ItemClassification.useful]
        self.add_to_pool(item_pool, other_useful_items)

        # Get count of non event locations
        non_events = len([location for location in self.multiworld.get_locations(self.player)
                          if location.name not in event_data_table.keys()])

        filler_count = non_events - len(item_pool)

        # Add filler items to the pool
        for _ in range(filler_count):
            filler = self.get_filler_item_name()
            self.used_items.add(filler)
            item_pool.append(self.create_item(filler))

        self.multiworld.itempool += item_pool

    def add_to_pool(self, item_pool, other_useful_items):
        for name in other_useful_items:
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
        location_data = location_data_table[location_name]
        return location_data.classification

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choices(filler_items, weights=filler_weights)[0]

    def set_rules(self) -> None:
        # Set location rules
        for location in self.multiworld.get_locations(self.player):
            # Use location rule table if available
            if location.name in location_rule_data_table:
                add_rule(location, self.create_rule(location.name))

        # Set entrance rules
        for region in self.multiworld.regions:
            if region.player != self.player:
                continue
            for entrance in region.exits:
                if entrance.name in entrance_rule_data_table:
                    add_rule(entrance, self.create_entrance_rule(entrance.name))

        # Set event locked items
        for event_name, e_data in event_data_table.items():
            location = self.multiworld.get_location(event_name, self.player)
            location.place_locked_item(self.create_event(e_data.item))

        # Set item rules
        for (location_name, rule) in item_rule_data_table.items():
            location = self.multiworld.get_location(location_name, self.player)
            add_item_rule(location, rule)
            add_item_rule(location, lambda i: i.player == self.player)

        # Completion condition.
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_rule(self, location_name: str) -> Callable[[CollectionState], bool]:
        return lambda state: location_rule_data_table[location_name](state, self.player)

    def create_chara_rule(self, location_name: str) -> Callable[[CollectionState], bool]:
        # LRFF13 uses explicit rule tables; no extra character scaling.
        return lambda state: True

    def create_entrance_rule(self, entrance_name: str) -> Callable[[CollectionState], bool]:
        return lambda state: entrance_rule_data_table[entrance_name](state, self.player)

    def create_event(self, event_item: str) -> LRFF13Item:
        name = event_item
        return LRFF13Item(name, ItemClassification.progression, None, self.player)

    def generate_early(self) -> None:
        # LRFF13 currently has no early-generation shuffling requirements.
        # Reserved for potential universal tracker passthrough support.
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

        # Build local item placements for the same player that have items in their own world
        local_item_placements: List[Dict[str, Any]] = []
        for loc in self.multiworld.get_locations(self.player):
            if loc.name in event_data_table:
                continue
            # Only include locations that have an item placed
            if getattr(loc, "item", None) is None:
                continue
            item = loc.item
            if item.player != self.player:
                continue
            local_item_placements.append({
                "location_id": location_data_table[loc.name].str_id,
                "item_id": item_data_table[item.name].str_id
            })

        seed_name = self.multiworld.seed_name + "_" + self.multiworld.get_player_name(self.player)
        data = {
            "seed": seed_name,  # to identify the seed
            "type": "archipelago",  # to identify the seed type
            # Fields consumed by the LR mod tool
            "version": LRFF13_VERSION,
            # Retain archipelago details for debugging/auxiliary tools
            "archipelago": {
                "version": LRFF13_VERSION,
                "used_items": list(self.used_items),
                "spheres": spheres,
                "item_placements": item_placements,
                "local_item_placements": local_item_placements
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
        return {}

    # From Tunic implementation
    # For the universal tracker, doesn't get called in standard gen
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data
