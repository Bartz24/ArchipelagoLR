from typing import Callable, Dict, List
from BaseClasses import CollectionState
from .RuleLogic import state_has_at_least

rule_data_list: List[Callable[[CollectionState, int], bool]] = [
    lambda state, player:
    True,  # Rule 0
    lambda state, player:
    state.has("Eradia", player, 100),  # Rule 1
    lambda state, player:
    state.has("Tablet", player, 3),  # Rule 2
    lambda state, player:
    state.has("Tablet", player, 2),  # Rule 3
    lambda state, player:
    (state.has("Arithmometer", player) and
     state.has("Eradia", player, 100)),  # Rule 4
    lambda state, player:
    (state.has("Loupe", player) and
     state.has("Eradia", player, 100)),  # Rule 5
    lambda state, player:
    (state.has("Monster Flesh", player) and
     state.has("Eradia", player, 700)),  # Rule 6
    lambda state, player:
    (state.has("Tablet", player) and
     state.has("Eradia", player, 200)),  # Rule 7
    lambda state, player:
    state.has("Eradia", player, 700),  # Rule 8
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("Crux Base", player) and
     state.has("Crux Tip", player) and
     state.has("Crux Body", player) and
     state.has("Eradia", player, 100)),  # Rule 9
    lambda state, player:
    state.has("Eradia", player, 200),  # Rule 10
    lambda state, player:
    (state.has("Supply Sphere Password", player) and
     state.has("Eradia", player, 200)),  # Rule 11
    lambda state, player:
    state.has("Eradia", player, 300),  # Rule 12
    lambda state, player:
    (state.has("Thunderclap Cap", player) and
     state.has("Shaolong Gui Shell", player) and
     state.has("Mandragora Root", player) and
     state.has("Eradia", player, 200)),  # Rule 13
    lambda state, player:
    ((state.has("Green Carbuncle Doll", player) or
      state.has("Red Carbuncle Doll", player)) and
      state.has("Eradia", player, 200)),  # Rule 14
    lambda state, player:
    (state.has("Spectral Elixir", player) and
     state.has("Eradia", player, 200)),  # Rule 15
    lambda state, player:
    (state.has("Cursed Dragon Claw", player) and
     state.has("Eradia", player, 200)),  # Rule 16
    lambda state, player:
    (state.has("Rubber Ball", player) and
     state.has("Eradia", player, 100)),  # Rule 17
    lambda state, player:
    state.has("Eradia", player, 600),  # Rule 18
    lambda state, player:
    state.has("Eradia", player, 400),  # Rule 19
    lambda state, player:
    (state.has("Quill Pen", player) and
     state.has("Eradia", player, 500)),  # Rule 20
    lambda state, player:
    (state.has("Phantom Rose", player) and
     state.has("Eradia", player, 300)),  # Rule 21
    lambda state, player:
    state.has("Eradia", player, 500),  # Rule 22
    lambda state, player:
    state.has("Gysahl Greens", player),  # Rule 23
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 300)),  # Rule 24
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200)),  # Rule 25
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100)),  # Rule 26
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Data Recorder", player) and
     state.has("Eradia", player, 300)),  # Rule 27
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 400)),  # Rule 28
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Aryas Apple", player, 2) and
     state.has("Eradia", player, 200)),  # Rule 29
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Fragment of Mischief", player) and
     state.has("Fragment of Radiance", player) and
     state.has("Fragment of Smiles", player) and
     state.has("Fragment of Courage", player) and
     state.has("Fragment of Kindness", player) and
     state.has("Eradia", player, 200)),  # Rule 30
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Goddess Glyphs", player) and
     state.has("Chaos Glyphs", player) and
     state.has("Plate Metal Fragment", player) and
     state.has("Silvered Metal Fragment", player) and
     state.has("Golden Metal Fragment", player)),  # Rule 31
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Goddess Glyphs", player) and
     state.has("Chaos Glyphs", player) and
     state.has("Eradia", player, 200)),  # Rule 32
    lambda state, player:
    (state.has("ID Card", player) and
     state.has("Sneaking-In Special Ticket", player)),  # Rule 33
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 400)),  # Rule 34
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200)),  # Rule 35
    lambda state, player:
    state.has("Musical Treasure Sphere Key", player),  # Rule 36
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Eradia", player, 200)),  # Rule 37
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Eradia", player, 300)),  # Rule 38
    lambda state, player:
    (state.has("ID Card", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200)),  # Rule 39
    lambda state, player:
    (state.has("Music Satchel", player) and
     state.has("Eradia", player, 200)),  # Rule 40
    lambda state, player:
    (state.has("Father's Letter", player) and
     state.has("Eradia", player, 200)),  # Rule 41
    lambda state, player:
    (state.has("Civet Musk", player) and
     state.has("Gordon Gourmet's Recipe", player) and
     state.has("Steak a la Civet", player) and
     state.has("Eradia", player, 300)),  # Rule 42
    lambda state, player:
    (state.has("Nostalgic Score: Chorus", player) and
     state.has("Nostalgic Score: Refrain", player) and
     state.has("Nostalgic Score: Coda", player) and
     state.has("Eradia", player, 200)),  # Rule 43
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Eradia", player, 300)),  # Rule 44
    lambda state, player:
    state.has("Civet Musk", player),  # Rule 45
    lambda state, player:
    (state.has("Civet Musk", player) and
     state.has("Gordon Gourmet's Recipe", player) and
     state.has("Eradia", player, 200)),  # Rule 46
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 300)),  # Rule 47
    lambda state, player:
    state.has("Eradia", player, 800),  # Rule 48
    lambda state, player:
    state.has("Eradia", player, 900),  # Rule 49
    lambda state, player:
    state.has("Eradia", player, 1000),  # Rule 50
    lambda state, player:
    state.has("Eradia", player, 1100),  # Rule 51
    lambda state, player:
    state.has("Eradia", player, 1200),  # Rule 52
    lambda state, player:
    state.has("Eradia", player, 1300),  # Rule 53
    lambda state, player:
    state.has("Eradia", player, 1400),  # Rule 54
    lambda state, player:
    (state.has("Proof of Legendary Title", player) and
     state.has("Eradia", player, 300)),  # Rule 55
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 500)),  # Rule 56
    lambda state, player:
    (state.has("Jade Hair Comb", player) and
     state.has("Bronze Pocket Watch", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200)),  # Rule 57
    lambda state, player:
    (state.has("Chocobo Girl's Phone No.", player) and
     state.has("ID Card", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200)),  # Rule 58
    lambda state, player:
    (state.has("Beloved's Gift", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200)),  # Rule 59
    lambda state, player:
    (state.has("Key to the Sand Gate", player) and
     state.has("Key to the Green Gate", player) and
     state.has("Eradia", player, 900)),  # Rule 60
    lambda state, player:
    (state.has("Bandit's Bloodseal", player) and
     state.has("Oath of the Merchants Guild", player) and
     state.has("Eradia", player, 900)),  # Rule 61
    lambda state, player:
    (state.has("Proof of Courage", player) and
     state.has("Eradia", player, 200)),  # Rule 62
    lambda state, player:
    (state.has("Violet Amulet", player) and
     state.has("Eradia", player, 200)),  # Rule 63
    lambda state, player:
    (state.has("Lapis Lazuli", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 200)),  # Rule 64
    lambda state, player:
    (state.has("Power Booster", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 300)),  # Rule 65
    lambda state, player:
    (state.has("Moogle Dust", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100)),  # Rule 66
    lambda state, player:
    (state.has("Old-Fashioned Photo Frame", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100)),  # Rule 67
    lambda state, player:
    (state.has("Etro's Forbidden Tome", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200)),  # Rule 68
    lambda state, player:
    (state.has("Broken Gyroscope", player) and
     state.has("Eradia", player, 200)),  # Rule 69
    lambda state, player:
    (state.has("Golden Scarab", player) and
     state.has("Tablet", player, 2) and
     state.has("Eradia", player, 200)),  # Rule 70
    lambda state, player:
    state.has("Seedhunter Membership Card", player),  # Rule 71
    lambda state, player:
    (state.has("Seedhunter Membership Card", player) and
     state.has("Moogle Fragment", player)),  # Rule 72
    lambda state, player:
    state.has("Loupe", player),  # Rule 73
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Eradia", player, 200)),  # Rule 74
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("Eradia", player, 100)),  # Rule 75
    lambda state, player:
    (state.has("Beloved's Gift", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100)),  # Rule 76
    lambda state, player:
    (state.has("Moogle Fragment", player) and
     state.has("Gysahl Greens", player) and
     state.has("Seedhunter Membership Card", player) and
     state.has("Eradia", player, 100)),  # Rule 77
]

rule_data_table: Dict[str, Callable[[CollectionState, int], bool]] = {
    "Golden Scarab Treasure (1)": rule_data_list[0],
    "Oasis Lighthouse Treasure (1)": rule_data_list[0],
    "Grave of the Colossi Shrine Treasure (1)": rule_data_list[0],
    "Giant's Sandbox Treasure (1)": rule_data_list[0],
    "Golden Chamber Lower Treasure (1)": rule_data_list[0],
    "Giant's Sandbox Treasure (2)": rule_data_list[0],
    "Giant's Sandbox Treasure (3)": rule_data_list[0],
    "Giant's Sandbox Treasure (4)": rule_data_list[0],
    "Ruffian Outdoor Treasure (1)": rule_data_list[0],
    "Dry Floodlands Treasure (1)": rule_data_list[0],
    "Oasis Lighthouse Treasure (2)": rule_data_list[0],
    "Oasis Lighthouse Treasure (3)": rule_data_list[0],
    "Atomos's Sand Treasure (1)": rule_data_list[0],
    "Grave of the Colossi Treasure (1)": rule_data_list[0],
    "Grave of the Colossi Treasure (2)": rule_data_list[0],
    "Grave of the Colossi Treasure (3)": rule_data_list[0],
    "Atomos's Sand Treasure (2)": rule_data_list[0],
    "Ruffian 2nd Floor Treasure (1)": rule_data_list[0],
    "Temple Ruins Chamber of Dusk (Upper) Treasure (1)": rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Upper) Treasure (1)": rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Upper) Treasure (2)": rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Upper) Treasure (3)": rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Lower) Treasure (1)": rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Lower) Treasure (2)": rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Lower) Treasure (3)": rule_data_list[0],
    "Temple Ruins Sacred Grove Treasure (1)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Treasure (1)": rule_data_list[0],
    "Dry Floodlands Shrine Treasure (1)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Treasure (1)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Treasure (2)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Treasure (3)": rule_data_list[0],
    "Temple Ruins Scorched Earth (Lower) Treasure (1)": rule_data_list[0],
    "Temple Ruins Scorched Earth (Upper) Treasure (1)": rule_data_list[0],
    "Temple Ruins Scorched Earth (Upper) Treasure (2)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Treasure (2)": rule_data_list[0],
    "Atomos's Sands Shrine Treasure (1)": rule_data_list[0],
    "Giant's Sandbox Treasure (5)": rule_data_list[0],
    "Dry Floodlands Treasure (2)": rule_data_list[0],
    "Grave of the Colossi Shrine Tablet (1)": rule_data_list[1],
    "Dry Floodlands Shrine Tablet (1)": rule_data_list[1],
    "Atomos's Sands Shrine Tablet (1)": rule_data_list[1],
    "Temple Ruins Mural Crux Base (1)": rule_data_list[2],
    "Temple Ruins Mural Crux Body (1)": rule_data_list[3],
    "Temple Ruins Mural Crux Tip (1)": rule_data_list[3],
    "Temple Ruins Bhakti Reward (1)": rule_data_list[1],
    "Grave of the Colossi Pilgrim's Crux (1)": rule_data_list[0],
    "Temple Ruins Scorched Earth Pilgrim's Crux (1)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (1)": rule_data_list[0],
    "Temple Ruins Scorched Earth Pilgrim's Crux (2)": rule_data_list[0],
    "Dry Floodlands Pilgrim's Crux (1)": rule_data_list[0],
    "Atomos's Sands Pilgrim's Crux (1)": rule_data_list[0],
    "Giant's Sandbox Pilgrim's Crux (1)": rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (1)": rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (2)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (1)": rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (3)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (2)": rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (4)": rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (2)": rule_data_list[0],
    "Atomos's Sands Loupe (1)": rule_data_list[0],
    "The Life of a Machine Quest (1)": rule_data_list[1],
    "The Life of a Machine Quest (2)": rule_data_list[1],
    "Old Rivals Quest (1)": rule_data_list[4],
    "Old Rivals Quest (2)": rule_data_list[4],
    "His Wife's Dream Quest (1)": rule_data_list[4],
    "His Wife's Dream Quest (2)": rule_data_list[4],
    "Tool of the Trade Quest (1)": rule_data_list[5],
    "Tool of the Trade Quest (2)": rule_data_list[5],
    "Adonis's Audition Quest (1)": rule_data_list[1],
    "Adonis's Audition Quest (2)": rule_data_list[1],
    "What Rough Beast Slouches Quest (1)": rule_data_list[6],
    "What Rough Beast Slouches Quest (2)": rule_data_list[6],
    "Skeletons In The Closet Quest (1)": rule_data_list[7],
    "Skeletons In The Closet Quest (2)": rule_data_list[7],
    "Last One Standing Quest (1)": rule_data_list[8],
    "Last One Standing Quest (2)": rule_data_list[8],
    "Last One Standing Quest (3)": rule_data_list[8],
    "What Rough Beast Slouches Libra Notes (1)": rule_data_list[0],
    "Dead Dunes Boss Drop (1)": rule_data_list[9],
    "Aeronite Missable Drop (1)": rule_data_list[8],
    "Cathedral Proof Of Courage (1)": rule_data_list[10],
    "Pilgrim's Passage Violet Amulet Treasure (1)": rule_data_list[0],
    "North Station Plaza Treasure (1)": rule_data_list[0],
    "The Avenue Treasure (1)": rule_data_list[0],
    "Gallery Steps Treasure (1)": rule_data_list[0],
    "2nd Ave Treasure (1)": rule_data_list[0],
    "Pilgrim's Passage (Grassy) Treasure (1)": rule_data_list[0],
    "Old Theater Platform Treasure (1)": rule_data_list[0],
    "The Warren Mangled Hill Treasure (1)": rule_data_list[0],
    "South Station (Supply Sphere) Treasure (1)": rule_data_list[11],
    "Warehouse District (Supply Sphere) Treasure (1)": rule_data_list[11],
    "Residences (Supply Sphere) Treasure (1)": rule_data_list[11],
    "Forsaken Graveyard Treasure (1)": rule_data_list[10],
    "Den Of Shadows Treasure (1)": rule_data_list[10],
    "Luxerion After 1st Phone (1)": rule_data_list[0],
    "Den Of Shadows Treasure (2)": rule_data_list[10],
    "Luxerion After 1st Phone (2)": rule_data_list[0],
    "Luxerion After 1st Phone (3)": rule_data_list[0],
    "Luxerion Marketplace Treasure (1)": rule_data_list[0],
    "Forsaken Graveyard Treasure (2)": rule_data_list[10],
    "1st Ave Rubber Ball (1)": rule_data_list[1],
    "Marketplace Doll (1)": rule_data_list[10],
    "North Station Plaza Doll (1)": rule_data_list[10],
    "Warehouse District Thunderclap Cap (1)": rule_data_list[0],
    "Luxerion Proof of Legendary Title (1)": rule_data_list[10],
    "Luxerion Ghost Phantom Rose (1)": rule_data_list[12],
    "Luxerion Marketplace Pen (1)": rule_data_list[12],
    "Baird Seedhunter Membership Card (1)": rule_data_list[0],
    "Virgil Supply Sphere Password (1)": rule_data_list[10],
    "Buy Shaolong Gui Shell (1)": rule_data_list[0],
    "Buy Mandragora Root (1)": rule_data_list[1],
    "Chocobo Emporium Spectral Elixir (1)": rule_data_list[13],
    "The Things She Lost Quest (1)": rule_data_list[14],
    "The Things She Lost Quest (2)": rule_data_list[14],
    "Where Are You, Holmes? Quest (1)": rule_data_list[1],
    "Where Are You, Holmes? Quest (2)": rule_data_list[1],
    "Where Are You, Holmes? Quest (3)": rule_data_list[1],
    "Like Clockwork Quest (1)": rule_data_list[10],
    "Like Clockwork Quest (2)": rule_data_list[10],
    "Dying Wish Quest (1)": rule_data_list[15],
    "Dying Wish Quest (2)": rule_data_list[15],
    "Suspicious Spheres Quest (1)": rule_data_list[11],
    "Suspicious Spheres Quest (2)": rule_data_list[11],
    "Born From Chaos Quest (1)": rule_data_list[16],
    "Born From Chaos Quest (2)": rule_data_list[16],
    "Born From Chaos Quest (3)": rule_data_list[16],
    "Born From Chaos Quest (4)": rule_data_list[16],
    "Soul Seeds Quest (1)": rule_data_list[10],
    "Soul Seeds Quest (2)": rule_data_list[10],
    "Faster Than Lightning Quest (1)": rule_data_list[10],
    "Faster Than Lightning Quest (2)": rule_data_list[10],
    "Treasured Ball Quest (1)": rule_data_list[17],
    "Treasured Ball Quest (2)": rule_data_list[17],
    "Talbot's Gratitude (1)": rule_data_list[17],
    "The Angel's Tears Quest (1)": rule_data_list[18],
    "The Angel's Tears Quest (2)": rule_data_list[18],
    "The Saint's Stone Quest (1)": rule_data_list[10],
    "The Saint's Stone Quest (2)": rule_data_list[10],
    "The Saint's Stone Quest (3)": rule_data_list[10],
    "Aremiah Service Entrance Key (1)": rule_data_list[10],
    "Whither Faith Quest (1)": rule_data_list[1],
    "Whither Faith Quest (2)": rule_data_list[1],
    "The Avid Reader Quest (1)": rule_data_list[19],
    "The Avid Reader Quest (2)": rule_data_list[19],
    "Buried Passion Quest (1)": rule_data_list[20],
    "Buried Passion Quest (2)": rule_data_list[20],
    "The Girl Who Cried Wolf Quest (1)": rule_data_list[12],
    "The Girl Who Cried Wolf Quest (2)": rule_data_list[12],
    "Stuck in a Gem Quest (1)": rule_data_list[10],
    "Stuck in a Gem Quest (2)": rule_data_list[10],
    "Get the Girl Quest (1)": rule_data_list[10],
    "Get the Girl Quest (2)": rule_data_list[10],
    "A Rose By Any Other Name Quest (1)": rule_data_list[21],
    "A Rose By Any Other Name Quest (2)": rule_data_list[21],
    "A Rose By Any Other Name Quest (3)": rule_data_list[21],
    "A Rose By Any Other Name Quest (4)": rule_data_list[21],
    "Voices from the Grave Quest (1)": rule_data_list[12],
    "Voices from the Grave Quest (2)": rule_data_list[12],
    "To Save the Sinless Quest (1)": rule_data_list[22],
    "To Save the Sinless Quest (2)": rule_data_list[22],
    "Replace Chronostasis (1)": rule_data_list[1],
    "Luxerion Boss Drop (1)": rule_data_list[10],
    "Luxerion Boss+ Only Missable Drop (1)": rule_data_list[22],
    "Moogle Village Moogle Dust Treasure (1)": rule_data_list[0],
    "Research Camp Photo Frame Treasure (1)": rule_data_list[0],
    "Poltae Etro's Forbidden Tome (1)": rule_data_list[0],
    "Eremite Plains Broken Gyroscope Treasure (1)": rule_data_list[23],
    "Aryas Village Treasure (1)": rule_data_list[0],
    "Jagd Woods Treasure (1)": rule_data_list[23],
    "The Grasslands Treasure (1)": rule_data_list[23],
    "Poltae Treasure (1)": rule_data_list[23],
    "Canopus Farms Treasure (1)": rule_data_list[0],
    "Rocky Crag Treasure (1)": rule_data_list[23],
    "The Grasslands Treasure (2)": rule_data_list[23],
    "Aryas Village Treasure (2)": rule_data_list[0],
    "The Grasslands Treasure (3)": rule_data_list[23],
    "Eremite Plains Treasure (1)": rule_data_list[23],
    "Eremite Plains Treasure (2)": rule_data_list[23],
    "Moogle Village Treasure (1)": rule_data_list[23],
    "City of Ruins Treasure (1)": rule_data_list[23],
    "Rocky Crag Treasure (2)": rule_data_list[23],
    "Rocky Crag Treasure (3)": rule_data_list[23],
    "Aryas Village Treasure (3)": rule_data_list[23],
    "Poltae Treasure (2)": rule_data_list[0],
    "Eremite Plains Crash Site Fragment (1)": rule_data_list[23],
    "Goddess Temple Treasure (1)": rule_data_list[24],
    "Goddess Temple Treasure (2)": rule_data_list[24],
    "Goddess Temple Treasure (3)": rule_data_list[24],
    "Goddess Temple Treasure (4)": rule_data_list[24],
    "Goddess Temple Treasure (5)": rule_data_list[24],
    "Goddess Temple Treasure (6)": rule_data_list[24],
    "Goddess Temple Treasure (7)": rule_data_list[24],
    "Goddess Temple Treasure (8)": rule_data_list[24],
    "Goddess Temple Treasure (9)": rule_data_list[24],
    "Dr Gysahl's Gysahl Greens (1)": rule_data_list[0],
    "Aryas Village Beloved's Gift Treasure (1)": rule_data_list[0],
    "Sarala Vegatable Seeds (1)": rule_data_list[23],
    "A Father's Request Quest (1)": rule_data_list[25],
    "A Father's Request Quest (2)": rule_data_list[25],
    "The Hunter's Challenge Quest (1)": rule_data_list[24],
    "The Hunter's Challenge Quest (2)": rule_data_list[24],
    "The Hunter's Challenge Quest (3)": rule_data_list[24],
    "A Final Cure Quest (1)": rule_data_list[25],
    "A Final Cure Quest (2)": rule_data_list[25],
    "A Final Cure Quest (3)": rule_data_list[25],
    "Fuzzy Search Quest (1)": rule_data_list[10],
    "Fuzzy Search Quest (2)": rule_data_list[10],
    "Fuzzy Search Quest (3)": rule_data_list[10],
    "Round 'em Up Quest (1)": rule_data_list[25],
    "Round 'em Up Quest (2)": rule_data_list[25],
    "Chocobo Cheer Quest (1)": rule_data_list[25],
    "Chocobo Cheer Quest (2)": rule_data_list[25],
    "Chocobo Cheer Quest (3)": rule_data_list[25],
    "Peace and Quiet, Kupo Quest (1)": rule_data_list[1],
    "Peace and Quiet, Kupo Quest (2)": rule_data_list[1],
    "Peace and Quiet, Kupo Quest (3)": rule_data_list[1],
    "Saving an Angel Quest (1)": rule_data_list[26],
    "Saving an Angel Quest (2)": rule_data_list[26],
    "Omega Point Quest (1)": rule_data_list[27],
    "Omega Point Quest (2)": rule_data_list[27],
    "The Old Man and the Field Quest (1)": rule_data_list[24],
    "The Old Man and the Field Quest (2)": rule_data_list[24],
    "Land of our Forebears Quest (1)": rule_data_list[28],
    "Land of our Forebears Quest (2)": rule_data_list[28],
    "A Taste of the Past Quest (1)": rule_data_list[29],
    "A Taste of the Past Quest (2)": rule_data_list[29],
    "A Taste of the Past Quest (3)": rule_data_list[29],
    "Dog, Doctor and Assistant Quest (1)": rule_data_list[25],
    "Dog, Doctor and Assistant Quest (2)": rule_data_list[25],
    "Main Quest 5 (1)": rule_data_list[30],
    "Main Quest 5 (2)": rule_data_list[30],
    "Main Quest 5 (3)": rule_data_list[30],
    "The Right Stuff Quest (1)": rule_data_list[25],
    "The Right Stuff Quest (2)": rule_data_list[25],
    "The Secret Lives of Sheep Quest (1)": rule_data_list[24],
    "The Secret Lives of Sheep Quest (2)": rule_data_list[24],
    "Where Are You, Moogle? Quest (1)": rule_data_list[1],
    "Where Are You, Moogle? Quest (2)": rule_data_list[1],
    "Where Are You, Moogle? Quest (3)": rule_data_list[1],
    "Mercy of a Goddess Quest (1)": rule_data_list[24],
    "Mercy of a Goddess Quest (2)": rule_data_list[24],
    "The Grail of Valhalla Quest (1)": rule_data_list[31],
    "The Grail of Valhalla Quest (2)": rule_data_list[31],
    "The Grail of Valhalla Quest (3)": rule_data_list[31],
    "To Live in Chaos Quest (1)": rule_data_list[28],
    "To Live in Chaos Quest (2)": rule_data_list[28],
    "To Live in Chaos Quest (3)": rule_data_list[28],
    "Killing Time Quest (1)": rule_data_list[26],
    "Killing Time Quest (2)": rule_data_list[26],
    "Matchmaker Quest (1)": rule_data_list[25],
    "Matchmaker Quest (2)": rule_data_list[25],
    "Mother and Daughter Quest (1)": rule_data_list[25],
    "Mother and Daughter Quest (2)": rule_data_list[25],
    "The Secret Lives of Sheep Mystery Egg (1)": rule_data_list[24],
    "Goddess Temple Goddess Glyphs (1)": rule_data_list[25],
    "Goddess Temple Chaos Glyphs (1)": rule_data_list[25],
    "Poltae Plate Metal Fragment (1)": rule_data_list[32],
    "Poltae Silvered Metal Fragment (1)": rule_data_list[32],
    "Poltae Gold Metal Fragment (1)": rule_data_list[32],
    "Research Camp Data Recorder (1)": rule_data_list[25],
    "Aryas Village Apple (1)": rule_data_list[25],
    "Aryas Village Apple (2)": rule_data_list[25],
    "Aryas Village Apple (3)": rule_data_list[25],
    "Wildlands Boss Drop (1)": rule_data_list[24],
    "Reveler's Quarter Lapis Lazuli Treasure (1)": rule_data_list[0],
    "Industrial Area Power Booster (1)": rule_data_list[33],
    "Tunnel Oath of the Merchants Guild Treasure (1)": rule_data_list[0],
    "Industrial Area Jade Hair Comb (1)": rule_data_list[34],
    "Industrial Area Bronze Pocket Watch (1)": rule_data_list[35],
    "Chocobo Girl Poster (1)": rule_data_list[0],
    "Glutton's Quarter Treasure (1)": rule_data_list[0],
    "Aromatic Market Treasure (1)": rule_data_list[0],
    "Central Ave Treasure (1)": rule_data_list[0],
    "Coliseum Square Treasure (1)": rule_data_list[0],
    "Tour Guide Sneaking-In Special Ticket (1)": rule_data_list[0],
    "Warehouse District Id Card (1)": rule_data_list[35],
    "Coliseum Square (Musical) Treasure (1)": rule_data_list[36],
    "Cactuar Statue (Musical) Treasure (1)": rule_data_list[36],
    "Station (Musical) Treasure (1)": rule_data_list[36],
    "Cactuar Statue Treasure (1)": rule_data_list[0],
    "Reveler's Quarter Treasure (1)": rule_data_list[0],
    "Augur's Quarter Treasure (1)": rule_data_list[37],
    "Patron's Palace Treasure (1)": rule_data_list[38],
    "Hawker's Row Treasure (1)": rule_data_list[0],
    "Augur's Quarter Treasure (2)": rule_data_list[37],
    "Warehouse District Treasure (1)": rule_data_list[35],
    "Augur's Quarter Treasure (3)": rule_data_list[39],
    "Supply Line Treasure (1)": rule_data_list[35],
    "Industrial Area Treasure (1)": rule_data_list[35],
    "Lower City Treasure (1)": rule_data_list[0],
    "Glutton's Quarter Treasure (2)": rule_data_list[0],
    "Reveler's Quarter Treasure (2)": rule_data_list[0],
    "Patron's Palace Treasure (2)": rule_data_list[38],
    "Patron's Palace Treasure (3)": rule_data_list[38],
    "Patron's Palace Treasure (4)": rule_data_list[38],
    "Patron's Palace Treasure (5)": rule_data_list[38],
    "Slaughterhouse Special Fragment of Courage (1)": rule_data_list[25],
    "Slaughterhouse (1)": rule_data_list[0],
    "Slaughterhouse (2)": rule_data_list[0],
    "Slaughterhouse (3)": rule_data_list[0],
    "Slaughterhouse (4)": rule_data_list[0],
    "Slaughterhouse (5)": rule_data_list[0],
    "Slaughterhouse (6)": rule_data_list[0],
    "Slaughterhouse (7)": rule_data_list[0],
    "Slaughterhouse (8)": rule_data_list[0],
    "Slaughterhouse (9)": rule_data_list[0],
    "Slaughterhouse (10)": rule_data_list[0],
    "The Fighting Actress Slaughterhouse (1)": rule_data_list[37],
    "The Fighting Actress Slaughterhouse (2)": rule_data_list[37],
    "The Fighting Actress Slaughterhouse (3)": rule_data_list[37],
    "The Fighting Actress Slaughterhouse (4)": rule_data_list[37],
    "Tanbam's Taboo Slaughterhouse (1)": rule_data_list[34],
    "Chocobo Girl Miqo'te Dress (1)": rule_data_list[0],
    "Director Femme Fetale (1)": rule_data_list[38],
    "Fireworks in a Bottle Quest (1)": rule_data_list[37],
    "Fireworks in a Bottle Quest (2)": rule_data_list[37],
    "The Fighting Actress Quest (1)": rule_data_list[37],
    "The Fighting Actress Quest (2)": rule_data_list[37],
    "Songless Diva Quest (1)": rule_data_list[40],
    "Songless Diva Quest (2)": rule_data_list[40],
    "Stolen Things Quest (1)": rule_data_list[41],
    "Stolen Things Quest (2)": rule_data_list[41],
    "Fireworks for a Steal Quest (1)": rule_data_list[37],
    "Fireworks for a Steal Quest (2)": rule_data_list[37],
    "A Testing Proposition Quest (1)": rule_data_list[22],
    "A Testing Proposition Quest (2)": rule_data_list[22],
    "Last Date Quest (1)": rule_data_list[34],
    "Last Date Quest (2)": rule_data_list[34],
    "Free Will Quest (1)": rule_data_list[12],
    "Free Will Quest (2)": rule_data_list[12],
    "Free Will Quest (3)": rule_data_list[12],
    "Friends Forever Quest (1)": rule_data_list[34],
    "Friends Forever Quest (2)": rule_data_list[34],
    "Friends Forever Quest (3)": rule_data_list[34],
    "Family Food Quest (1)": rule_data_list[42],
    "Family Food Quest (2)": rule_data_list[42],
    "Tanbam's Taboo Quest (1)": rule_data_list[34],
    "Tanbam's Taboo Quest (2)": rule_data_list[34],
    "Play It for Me Quest (1)": rule_data_list[43],
    "Play It for Me Quest (2)": rule_data_list[43],
    "Adoring Adornments Quest (1)": rule_data_list[44],
    "Adoring Adornments Quest (2)": rule_data_list[44],
    "Adoring Candice Quest (1)": rule_data_list[34],
    "Adoring Candice Quest (2)": rule_data_list[34],
    "Adoring Candice Quest (3)": rule_data_list[34],
    "Death Safari Quest (1)": rule_data_list[44],
    "Death Safari Quest (2)": rule_data_list[44],
    "Death Safari Quest (3)": rule_data_list[44],
    "Death Safari Quest (4)": rule_data_list[44],
    "Death Safari Quest (5)": rule_data_list[44],
    "Death Game Quest (1)": rule_data_list[44],
    "Death Game Quest (2)": rule_data_list[44],
    "Death Game Quest (3)": rule_data_list[44],
    "Morris Musical Treasure Sphere Key (1)": rule_data_list[10],
    "Patron's Palace Serah's Pendant (1)": rule_data_list[38],
    "Gordon Gourmet's Recipe (1)": rule_data_list[45],
    "Seedy Steak a la Civet (1)": rule_data_list[46],
    "Gregory Father's Letter (1)": rule_data_list[10],
    "Tanbam's Taboo Libra Notes (1)": rule_data_list[34],
    "Yusnaan Boss Drop (1)": rule_data_list[47],
    "Initial 3rd Garb (1)": rule_data_list[0],
    "Initial 3rd Garb (2)": rule_data_list[0],
    "Initial 3rd Garb (3)": rule_data_list[0],
    "Ark Day 1 (1)": rule_data_list[1],
    "Ark Day 1 (2)": rule_data_list[1],
    "Ark Day 1 (3)": rule_data_list[1],
    "Ark Day 1 (4)": rule_data_list[1],
    "Ark Day 1 (5)": rule_data_list[1],
    "Ark Day 2 (1)": rule_data_list[10],
    "Ark Day 2 (2)": rule_data_list[10],
    "Ark Day 2 (3)": rule_data_list[10],
    "Ark Day 3 (1)": rule_data_list[12],
    "Ark Day 4 (1)": rule_data_list[19],
    "Ark Day 4 (2)": rule_data_list[19],
    "Ark Day 5 (1)": rule_data_list[22],
    "Ark Day 6 (1)": rule_data_list[18],
    "Ark Day 7 (1)": rule_data_list[8],
    "Ark Day 8 (1)": rule_data_list[48],
    "Ark Day 9 (1)": rule_data_list[49],
    "Ark Day 10 (1)": rule_data_list[50],
    "Ark Day 11 (1)": rule_data_list[51],
    "Ark Day 12 (1)": rule_data_list[52],
    "Ark Final Day (1)": rule_data_list[53],
    "Ark Final Day (2)": rule_data_list[53],
    "Ark Final Day (3)": rule_data_list[53],
    "Ark Extra Day (1)": rule_data_list[54],
    "Replace Curaga (1)": rule_data_list[0],
    "Replace Teleport (1)": rule_data_list[0],
    "Replace Escape (1)": rule_data_list[0],
    "Flower in the Sands CoP Quest (1)": rule_data_list[1],
    "Flower in the Sands CoP Quest (2)": rule_data_list[1],
    "Biologically Speaking CoP Quest (1)": rule_data_list[1],
    "Biologically Speaking CoP Quest (2)": rule_data_list[1],
    "The Real Client CoP Quest (1)": rule_data_list[19],
    "The Real Client CoP Quest (2)": rule_data_list[19],
    "The Real Client CoP Quest (3)": rule_data_list[19],
    "For My Child CoP Quest (1)": rule_data_list[12],
    "For My Child CoP Quest (2)": rule_data_list[12],
    "For My Child CoP Quest (3)": rule_data_list[12],
    "Bandits' New Weapon CoP Quest (1)": rule_data_list[19],
    "Bandits' New Weapon CoP Quest (2)": rule_data_list[19],
    "Bandits' New Weapon CoP Quest (3)": rule_data_list[19],
    "Banned Goods CoP Quest (1)": rule_data_list[1],
    "Banned Goods CoP Quest (2)": rule_data_list[1],
    "Banned Goods CoP Quest (3)": rule_data_list[1],
    "Climbing The Ranks I CoP Quest (1)": rule_data_list[12],
    "Climbing The Ranks I CoP Quest (2)": rule_data_list[12],
    "Miracle Vintage CoP Quest (1)": rule_data_list[19],
    "Miracle Vintage CoP Quest (2)": rule_data_list[19],
    "Miracle Vintage CoP Quest (3)": rule_data_list[19],
    "Climbing The Ranks II CoP Quest (1)": rule_data_list[12],
    "Climbing The Ranks II CoP Quest (2)": rule_data_list[12],
    "Heightened Security CoP Quest (1)": rule_data_list[19],
    "Heightened Security CoP Quest (2)": rule_data_list[19],
    "Heightened Security CoP Quest (3)": rule_data_list[19],
    "Desert Cleanup CoP Quest (1)": rule_data_list[1],
    "Desert Cleanup CoP Quest (2)": rule_data_list[1],
    "Desert Cleanup CoP Quest (3)": rule_data_list[1],
    "A Treasure for a God CoP Quest (1)": rule_data_list[9],
    "A Treasure for a God CoP Quest (2)": rule_data_list[9],
    "Lucky Charm CoP Quest (1)": rule_data_list[1],
    "Lucky Charm CoP Quest (2)": rule_data_list[1],
    "Supply and Demand CoP Quest (1)": rule_data_list[12],
    "Supply and Demand CoP Quest (2)": rule_data_list[12],
    "Supply and Demand CoP Quest (3)": rule_data_list[12],
    "A New Application CoP Quest (1)": rule_data_list[42],
    "A New Application CoP Quest (2)": rule_data_list[42],
    "A New Application CoP Quest (3)": rule_data_list[42],
    "Pride And Greed I CoP Quest (1)": rule_data_list[12],
    "Pride And Greed I CoP Quest (2)": rule_data_list[12],
    "Pride And Greed I CoP Quest (3)": rule_data_list[12],
    "Pride And Greed II CoP Quest (1)": rule_data_list[8],
    "Pride And Greed II CoP Quest (2)": rule_data_list[8],
    "Pride And Greed II CoP Quest (3)": rule_data_list[8],
    "Pride And Greed III CoP Quest (1)": rule_data_list[49],
    "Pride And Greed III CoP Quest (2)": rule_data_list[49],
    "Pride And Greed III CoP Quest (3)": rule_data_list[49],
    "Revenge Is Sweet CoP Quest (1)": rule_data_list[1],
    "Revenge Is Sweet CoP Quest (2)": rule_data_list[1],
    "Gift of Gratitude CoP Quest (1)": rule_data_list[1],
    "Gift of Gratitude CoP Quest (2)": rule_data_list[1],
    "Gift of Gratitude CoP Quest (3)": rule_data_list[1],
    "A Song for God CoP Quest (1)": rule_data_list[12],
    "A Song for God CoP Quest (2)": rule_data_list[12],
    "A Song for God CoP Quest (3)": rule_data_list[12],
    "Slay the Machine CoP Quest (1)": rule_data_list[12],
    "Slay the Machine CoP Quest (2)": rule_data_list[12],
    "Enchanted Brush CoP Quest (1)": rule_data_list[22],
    "Enchanted Brush CoP Quest (2)": rule_data_list[22],
    "Enchanted Brush CoP Quest (3)": rule_data_list[22],
    "Heretics' Beasts CoP Quest (1)": rule_data_list[22],
    "Heretics' Beasts CoP Quest (2)": rule_data_list[22],
    "Heretics' Beasts CoP Quest (3)": rule_data_list[22],
    "Grave of a Bounty Hunter CoP Quest (1)": rule_data_list[22],
    "Grave of a Bounty Hunter CoP Quest (2)": rule_data_list[22],
    "Grave of a Bounty Hunter CoP Quest (3)": rule_data_list[22],
    "Inventive Seamstress CoP Quest (1)": rule_data_list[1],
    "Inventive Seamstress CoP Quest (2)": rule_data_list[1],
    "Puppeteer's Lament CoP Quest (1)": rule_data_list[22],
    "Puppeteer's Lament CoP Quest (2)": rule_data_list[22],
    "Puppeteer's Lament CoP Quest (3)": rule_data_list[22],
    "Revenge has Teeth CoP Quest (1)": rule_data_list[22],
    "Revenge has Teeth CoP Quest (2)": rule_data_list[22],
    "Night Patrol CoP Quest (1)": rule_data_list[22],
    "Night Patrol CoP Quest (2)": rule_data_list[22],
    "Night Patrol CoP Quest (3)": rule_data_list[22],
    "Trapped CoP Quest (1)": rule_data_list[1],
    "Trapped CoP Quest (2)": rule_data_list[1],
    "Trapped CoP Quest (3)": rule_data_list[1],
    "Trapped CoP Quest (4)": rule_data_list[1],
    "Mythical Badge CoP Quest (1)": rule_data_list[55],
    "Mythical Badge CoP Quest (2)": rule_data_list[55],
    "Mythical Badge CoP Quest (3)": rule_data_list[55],
    "Sun Flower CoP Quest (1)": rule_data_list[1],
    "Sun Flower CoP Quest (2)": rule_data_list[1],
    "Moon Flower CoP Quest (1)": rule_data_list[1],
    "Moon Flower CoP Quest (2)": rule_data_list[1],
    "Moon Flower CoP Quest (3)": rule_data_list[1],
    "Secret of the Chocoborel CoP Quest (1)": rule_data_list[12],
    "Secret of the Chocoborel CoP Quest (2)": rule_data_list[12],
    "Secret of the Chocoborel CoP Quest (3)": rule_data_list[12],
    "Wildlands In Danger! CoP Quest (1)": rule_data_list[24],
    "Wildlands In Danger! CoP Quest (2)": rule_data_list[24],
    "Wildlands In Danger! CoP Quest (3)": rule_data_list[24],
    "Hunting the Hunter CoP Quest (1)": rule_data_list[12],
    "Hunting the Hunter CoP Quest (2)": rule_data_list[12],
    "Hunting the Hunter CoP Quest (3)": rule_data_list[12],
    "Forget Me Not CoP Quest (1)": rule_data_list[1],
    "Forget Me Not CoP Quest (2)": rule_data_list[1],
    "Forget Me Not CoP Quest (3)": rule_data_list[1],
    "A Word of Thanks CoP Quest (1)": rule_data_list[12],
    "A Word of Thanks CoP Quest (2)": rule_data_list[12],
    "A Word of Thanks CoP Quest (3)": rule_data_list[12],
    "Fresh Fertilizer CoP Quest (1)": rule_data_list[28],
    "Fresh Fertilizer CoP Quest (2)": rule_data_list[28],
    "Fresh Fertilizer CoP Quest (3)": rule_data_list[28],
    "For the Future CoP Quest (1)": rule_data_list[12],
    "For the Future CoP Quest (2)": rule_data_list[12],
    "For the Future CoP Quest (3)": rule_data_list[12],
    "Dumpling Cook-Off CoP Quest (1)": rule_data_list[12],
    "Dumpling Cook-Off CoP Quest (2)": rule_data_list[12],
    "Dumpling Cook-Off CoP Quest (3)": rule_data_list[12],
    "Brain Over Brawn CoP Quest (1)": rule_data_list[8],
    "Brain Over Brawn CoP Quest (2)": rule_data_list[8],
    "Brain Over Brawn CoP Quest (3)": rule_data_list[8],
    "Hunter's Challenge CoP Quest (1)": rule_data_list[12],
    "Hunter's Challenge CoP Quest (2)": rule_data_list[12],
    "Hunter's Challenge CoP Quest (3)": rule_data_list[12],
    "A Secret Wish CoP Quest (1)": rule_data_list[12],
    "A Secret Wish CoP Quest (2)": rule_data_list[12],
    "A Secret Wish CoP Quest (3)": rule_data_list[12],
    "Moghan's Plea CoP Quest (1)": rule_data_list[1],
    "Moghan's Plea CoP Quest (2)": rule_data_list[1],
    "Moghan's Plea CoP Quest (3)": rule_data_list[1],
    "What's in a Brew? CoP Quest (1)": rule_data_list[56],
    "What's in a Brew? CoP Quest (2)": rule_data_list[56],
    "What's in a Brew? CoP Quest (3)": rule_data_list[56],
    "What's in a Brew? CoP Quest (4)": rule_data_list[56],
    "A Prayer to a Goddess CoP Quest (1)": rule_data_list[8],
    "A Prayer to a Goddess CoP Quest (2)": rule_data_list[8],
    "A Prayer to a Goddess CoP Quest (3)": rule_data_list[8],
    "Gatekeeper's Curiosity CoP Quest (1)": rule_data_list[22],
    "Gatekeeper's Curiosity CoP Quest (2)": rule_data_list[22],
    "Echoes of a Drum CoP Quest (1)": rule_data_list[12],
    "Echoes of a Drum CoP Quest (2)": rule_data_list[12],
    "Echoes of a Drum CoP Quest (3)": rule_data_list[12],
    "A Voice From Below CoP Quest (1)": rule_data_list[12],
    "A Voice From Below CoP Quest (2)": rule_data_list[12],
    "A Voice From Below CoP Quest (3)": rule_data_list[12],
    "Chocobo Chow CoP Quest (1)": rule_data_list[25],
    "Chocobo Chow CoP Quest (2)": rule_data_list[25],
    "Chocobo Chow CoP Quest (3)": rule_data_list[25],
    "Sylkis Secrets CoP Quest (1)": rule_data_list[24],
    "Sylkis Secrets CoP Quest (2)": rule_data_list[24],
    "Sylkis Secrets CoP Quest (3)": rule_data_list[24],
    "Digging Mole CoP Quest (1)": rule_data_list[25],
    "Digging Mole CoP Quest (2)": rule_data_list[25],
    "Digging Mole CoP Quest (3)": rule_data_list[25],
    "Two Together CoP Quest (1)": rule_data_list[12],
    "Two Together CoP Quest (2)": rule_data_list[12],
    "Two Together CoP Quest (3)": rule_data_list[12],
    "Emergency Treatment CoP Quest (1)": rule_data_list[25],
    "Emergency Treatment CoP Quest (2)": rule_data_list[25],
    "Emergency Treatment CoP Quest (3)": rule_data_list[25],
    "Moogle Gourmand CoP Quest (1)": rule_data_list[25],
    "Moogle Gourmand CoP Quest (2)": rule_data_list[25],
    "Moogle Gourmand CoP Quest (3)": rule_data_list[25],
    "Secret Machine CoP Quest (1)": rule_data_list[1],
    "Secret Machine CoP Quest (2)": rule_data_list[1],
    "Soulful Horn CoP Quest (1)": rule_data_list[10],
    "Soulful Horn CoP Quest (2)": rule_data_list[10],
    "Soulful Horn CoP Quest (3)": rule_data_list[10],
    "A Dangerous Cocktail CoP Quest (1)": rule_data_list[12],
    "A Dangerous Cocktail CoP Quest (2)": rule_data_list[12],
    "Source of Inspiration CoP Quest (1)": rule_data_list[22],
    "Source of Inspiration CoP Quest (2)": rule_data_list[22],
    "Youth Potion CoP Quest (1)": rule_data_list[8],
    "Youth Potion CoP Quest (2)": rule_data_list[8],
    "Youth Potion CoP Quest (3)": rule_data_list[8],
    "Beast Summoner CoP Quest (1)": rule_data_list[22],
    "Beast Summoner CoP Quest (2)": rule_data_list[22],
    "Beast Summoner CoP Quest (3)": rule_data_list[22],
    "What Seekers Seek CoP Quest (1)": rule_data_list[8],
    "What Seekers Seek CoP Quest (2)": rule_data_list[8],
    "What Seekers Seek CoP Quest (3)": rule_data_list[8],
    "True Colors CoP Quest (1)": rule_data_list[22],
    "True Colors CoP Quest (2)": rule_data_list[22],
    "True Colors CoP Quest (3)": rule_data_list[22],
    "Ultimate Craving CoP Quest (1)": rule_data_list[8],
    "Ultimate Craving CoP Quest (2)": rule_data_list[8],
    "Ultimate Craving CoP Quest (3)": rule_data_list[8],
    "Ultimate Craving CoP Quest (4)": rule_data_list[8],
    "Spell for Spell CoP Quest (1)": rule_data_list[8],
    "Spell for Spell CoP Quest (2)": rule_data_list[8],
    "Spell for Spell CoP Quest (3)": rule_data_list[8],
    "Unfired Firework CoP Quest (1)": rule_data_list[47],
    "Unfired Firework CoP Quest (2)": rule_data_list[47],
    "Unfired Firework CoP Quest (3)": rule_data_list[47],
    "Time Doesn't Heal CoP Quest (1)": rule_data_list[57],
    "Time Doesn't Heal CoP Quest (2)": rule_data_list[57],
    "Time Doesn't Heal CoP Quest (3)": rule_data_list[57],
    "A Man for a Chocobo Girl CoP Quest (1)": rule_data_list[58],
    "A Man for a Chocobo Girl CoP Quest (2)": rule_data_list[58],
    "A Man for a Chocobo Girl CoP Quest (3)": rule_data_list[58],
    "Rebuilding CoP Quest (1)": rule_data_list[47],
    "Rebuilding CoP Quest (2)": rule_data_list[47],
    "Global: Key To Her Heart CoP Quest (1)": rule_data_list[59],
    "Global: Key To Her Heart CoP Quest (2)": rule_data_list[59],
    "Global: Key To Her Heart CoP Quest (3)": rule_data_list[59],
    "Global: Roadworks I CoP Quest (1)": rule_data_list[49],
    "Global: Roadworks I CoP Quest (2)": rule_data_list[49],
    "Global: Roadworks I CoP Quest (3)": rule_data_list[49],
    "Global: Roadworks II CoP Quest (1)": rule_data_list[60],
    "Global: Roadworks II CoP Quest (2)": rule_data_list[60],
    "Global: Roadworks II CoP Quest (3)": rule_data_list[60],
    "Global: Roadworks III CoP Quest (1)": rule_data_list[61],
    "Global: Roadworks III CoP Quest (2)": rule_data_list[61],
    "Global: Roadworks III CoP Quest (3)": rule_data_list[61],
    "Global: A Girl's Challenge CoP Quest (1)": rule_data_list[62],
    "Global: A Girl's Challenge CoP Quest (2)": rule_data_list[62],
    "Global: What's Left Behind CoP Quest (1)": rule_data_list[63],
    "Global: What's Left Behind CoP Quest (2)": rule_data_list[63],
    "Global: Seeing The Dawn CoP Quest (1)": rule_data_list[64],
    "Global: Seeing The Dawn CoP Quest (2)": rule_data_list[64],
    "Global: Staying Sharp CoP Quest (1)": rule_data_list[65],
    "Global: Staying Sharp CoP Quest (2)": rule_data_list[65],
    "Global: Where Moogles Be CoP Quest (1)": rule_data_list[66],
    "Global: Where Moogles Be CoP Quest (2)": rule_data_list[66],
    "Global: Fading Prayer CoP Quest (1)": rule_data_list[67],
    "Global: Fading Prayer CoP Quest (2)": rule_data_list[67],
    "Global: Forbidden Tome CoP Quest (1)": rule_data_list[68],
    "Global: Forbidden Tome CoP Quest (2)": rule_data_list[68],
    "Global: Shoot For The Sky CoP Quest (1)": rule_data_list[69],
    "Global: Shoot For The Sky CoP Quest (2)": rule_data_list[69],
    "Global: Shoot For The Sky CoP Quest (3)": rule_data_list[69],
    "Global: Digging Mysteries CoP Quest (1)": rule_data_list[70],
    "Global: Digging Mysteries CoP Quest (2)": rule_data_list[70],
    "Global: Digging Mysteries CoP Quest (3)": rule_data_list[70],
    "10 Soul Seeds (1)": rule_data_list[71],
    "20 Soul Seeds (1)": rule_data_list[71],
    "30 Soul Seeds (1)": rule_data_list[71],
    "40 Soul Seeds (1)": rule_data_list[71],
    "50 Soul Seeds (1)": rule_data_list[71],
    "Soul Seeds Fragment of Radiance (1)": rule_data_list[72],
    "1 Unappraised (1)": rule_data_list[73],
    "5 Unappraised (1)": rule_data_list[73],
    "10 Unappraised (1)": rule_data_list[73],
    "20 Unappraised (1)": rule_data_list[73],
    "50 Unappraised (1)": rule_data_list[73],
    "Ultimate Lair Boss Drop (1)": rule_data_list[0],
    "Gorgonopsid Omega Drop (1)": rule_data_list[0],
    "Zaltys Omega Drop (1)": rule_data_list[0],
    "Miniflan Omega Drop (1)": rule_data_list[0],
    "Hanuman Omega Drop (1)": rule_data_list[0],
    "Zomok Omega Drop (1)": rule_data_list[0],
    "Goblin Omega Drop (1)": rule_data_list[0],
    "Gremlin Omega Drop (1)": rule_data_list[0],
    "Niblet Omega Drop (1)": rule_data_list[0],
    "Goblot Omega Drop (1)": rule_data_list[0],
    "Triffid Omega Drop (1)": rule_data_list[0],
    "Schrodinger Omega Drop (1)": rule_data_list[0],
    "Earth Eater Omega Drop (1)": rule_data_list[0],
    "Chocobo Eater Omega Drop (1)": rule_data_list[0],
    "Desert Sahagin Omega Drop (1)": rule_data_list[0],
    "Rafflesia Omega Drop (1)": rule_data_list[0],
    "Cactuar Omega Drop (1)": rule_data_list[0],
    "Gurangatch Omega Drop (1)": rule_data_list[0],
    "Skata'ne Omega Drop (1)": rule_data_list[0],
    "Dryad Omega Drop (1)": rule_data_list[0],
    "Dreadnought Omega Drop (1)": rule_data_list[0],
    "Hoplite Omega Drop (1)": rule_data_list[0],
    "Aster Protoflorian Omega Drop (1)": rule_data_list[0],
    "Gaunt Omega Drop (1)": rule_data_list[0],
    "Ectopudding Omega Drop (1)": rule_data_list[0],
    "Meonekton Omega Drop (1)": rule_data_list[0],
    "Cyclops Omega Drop (1)": rule_data_list[0],
    "Reaver Omega Drop (1)": rule_data_list[0],
    "Skeleton Omega Drop (1)": rule_data_list[0],
    "Ultimate Lair Floor 29 (1)": rule_data_list[0],
    "Ultimate Lair Floor 30 (1)": rule_data_list[0],
    "Ultimate Lair Floor 31 (1)": rule_data_list[0],
    "Ultimate Lair Floor 32 (1)": rule_data_list[0],
    "Ultimate Lair Boss Reward (1)": rule_data_list[0],
    "Arcangeli Omega Drop (1)": rule_data_list[53],
    "Sugriva Omega Drop (1)": rule_data_list[53],
    "Chimera Omega Drop (1)": rule_data_list[53],
    "Final Day Altar Of Salvation (1)": rule_data_list[53],
    "Final Day Altar Of Judgment (1)": rule_data_list[53],
    "Final Day Altar Of Atonement (1)": rule_data_list[53],
    "Final Day Altar Of Birth (1)": rule_data_list[53],
    "Final Day Temple Of Light (1)": rule_data_list[53],
    "Final Day Temple Of Light (2)": rule_data_list[53],
    "Final Day Temple Of Light (3)": rule_data_list[53],
    "Final Day Ultima Weapon (1)": rule_data_list[53],
    "Final Day Ultima Shield (1)": rule_data_list[53],
    "Cactair Fragment of Kindness (1)": rule_data_list[0],
    "Goblots Arithmometer (1)": rule_data_list[0],
    "Aeronite Monster Flesh (1)": rule_data_list[0],
    "Zomok Cursed Dragon Claw (1)": rule_data_list[0],
    "Gremlins Music Satchel (1)": rule_data_list[0],
    "Schrodinger Civet Musk (1)": rule_data_list[0],
    "Ark Day 0 Event (1)": rule_data_list[0],
    "Ark Day 1 Event (1)": rule_data_list[1],
    "Ark Day 2 Event (1)": rule_data_list[10],
    "Ark Day 3 Event (1)": rule_data_list[12],
    "Ark Day 4 Event (1)": rule_data_list[19],
    "Ark Day 5 Event (1)": rule_data_list[22],
    "Ark Day 6 Event (1)": rule_data_list[18],
    "Main Quest 4 Event (1)": rule_data_list[9],
    "Main Quest 1 Event (1)": rule_data_list[10],
    "Main Quest 3 Event (1)": rule_data_list[24],
    "Main Quest 2 Event (1)": rule_data_list[47],
    "Main Quest 5 Event (1)": rule_data_list[30],
    "The Things She Lost Quest Event (1)": rule_data_list[14],
    "Where Are You, Holmes? Quest Event (1)": rule_data_list[1],
    "Like Clockwork Quest Event (1)": rule_data_list[10],
    "Dying Wish Quest Event (1)": rule_data_list[15],
    "Suspicious Spheres Quest Event (1)": rule_data_list[11],
    "Born From Chaos Quest Event (1)": rule_data_list[16],
    "Soul Seeds Quest Event (1)": rule_data_list[10],
    "Faster Than Lightning Quest Event (1)": rule_data_list[10],
    "Treasured Ball Quest Event (1)": rule_data_list[17],
    "The Angel's Tears Quest Event (1)": rule_data_list[18],
    "The Saint's Stone Quest Event (1)": rule_data_list[10],
    "Whither Faith Quest Event (1)": rule_data_list[1],
    "The Avid Reader Quest Event (1)": rule_data_list[19],
    "Buried Passion Quest Event (1)": rule_data_list[20],
    "The Girl Who Cried Wolf Quest Event (1)": rule_data_list[12],
    "Stuck in a Gem Quest Event (1)": rule_data_list[10],
    "Get the Girl Quest Event (1)": rule_data_list[10],
    "A Rose By Any Other Name Quest Event (1)": rule_data_list[21],
    "Voices from the Grave Quest Event (1)": rule_data_list[12],
    "To Save the Sinless Quest Event (1)": rule_data_list[22],
    "The Life of a Machine Quest Event (1)": rule_data_list[1],
    "Old Rivals Quest Event (1)": rule_data_list[4],
    "His Wife's Dream Quest Event (1)": rule_data_list[4],
    "Tool of the Trade Quest Event (1)": rule_data_list[5],
    "Adonis's Audition Quest Event (1)": rule_data_list[1],
    "What Rough Beast Slouches Quest Event (1)": rule_data_list[6],
    "Skeletons In The Closet Quest Event (1)": rule_data_list[7],
    "Last One Standing Quest Event (1)": rule_data_list[8],
    "A Father's Request Quest Event (1)": rule_data_list[25],
    "The Hunter's Challenge Quest Event (1)": rule_data_list[24],
    "A Final Cure Quest Event (1)": rule_data_list[25],
    "Fuzzy Search Quest Event (1)": rule_data_list[10],
    "Round 'em Up Quest Event (1)": rule_data_list[25],
    "Chocobo Cheer Quest Event (1)": rule_data_list[25],
    "Peace and Quiet, Kupo Quest Event (1)": rule_data_list[1],
    "Saving an Angel Quest Event (1)": rule_data_list[26],
    "Omega Point Quest Event (1)": rule_data_list[27],
    "The Old Man and the Field Quest Event (1)": rule_data_list[24],
    "Land of our Forebears Quest Event (1)": rule_data_list[28],
    "A Taste of the Past Quest Event (1)": rule_data_list[29],
    "Dog, Doctor and Assistant Quest Event (1)": rule_data_list[25],
    "The Right Stuff Quest Event (1)": rule_data_list[25],
    "The Secret Lives of Sheep Quest Event (1)": rule_data_list[24],
    "Where Are You, Moogle? Quest Event (1)": rule_data_list[1],
    "Mercy of a Goddess Quest Event (1)": rule_data_list[24],
    "The Grail of Valhalla Quest Event (1)": rule_data_list[31],
    "To Live in Chaos Quest Event (1)": rule_data_list[28],
    "Killing Time Quest Event (1)": rule_data_list[26],
    "Matchmaker Quest Event (1)": rule_data_list[25],
    "Mother and Daughter Quest Event (1)": rule_data_list[25],
    "Fireworks in a Bottle Quest Event (1)": rule_data_list[37],
    "The Fighting Actress Quest Event (1)": rule_data_list[37],
    "Songless Diva Quest Event (1)": rule_data_list[40],
    "Stolen Things Quest Event (1)": rule_data_list[41],
    "Fireworks for a Steal Quest Event (1)": rule_data_list[37],
    "A Testing Proposition Quest Event (1)": rule_data_list[22],
    "Last Date Quest Event (1)": rule_data_list[34],
    "Free Will Quest Event (1)": rule_data_list[12],
    "Friends Forever Quest Event (1)": rule_data_list[34],
    "Family Food Quest Event (1)": rule_data_list[42],
    "Tanbam's Taboo Quest Event (1)": rule_data_list[34],
    "Play It for Me Quest Event (1)": rule_data_list[43],
    "Adoring Adornments Quest Event (1)": rule_data_list[44],
    "Adoring Candice Quest Event (1)": rule_data_list[34],
    "Death Safari Quest Event (1)": rule_data_list[44],
    "Death Game Quest Event (1)": rule_data_list[44],
    "0-1 Hint Event (1)": rule_data_list[0],
    "1-1 Hint Event (1)": rule_data_list[1],
    "1-2 Hint Event (1)": rule_data_list[10],
    "1-3 Hint Event (1)": rule_data_list[10],
    "1-4 Hint Event (1)": rule_data_list[10],
    "1-5 Hint Event (1)": rule_data_list[10],
    "2-1 Hint Event (1)": rule_data_list[37],
    "2-2 Hint Event (1)": rule_data_list[74],
    "2-3 Hint Event (1)": rule_data_list[47],
    "3-1 Hint Event (1)": rule_data_list[1],
    "3-2 Hint Event (1)": rule_data_list[25],
    "3-3 Hint Event (1)": rule_data_list[24],
    "4-1 Hint Event (1)": rule_data_list[1],
    "4-2 Hint Event (1)": rule_data_list[1],
    "4-3 Hint Event (1)": rule_data_list[1],
    "4-4 Hint Event (1)": rule_data_list[75],
    "4-5 Hint Event (1)": rule_data_list[9],
    "5-1 Hint Event (1)": rule_data_list[30],
    "5-2 Hint Event (1)": rule_data_list[26],
    "5-3 Hint Event (1)": rule_data_list[76],
    "5-4 Hint Event (1)": rule_data_list[77],
    "5-5 Hint Event (1)": rule_data_list[26],
    "5-6 Hint Event (1)": rule_data_list[1],
}
