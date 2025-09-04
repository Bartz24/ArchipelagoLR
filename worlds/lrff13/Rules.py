from typing import Callable, Dict, List
from BaseClasses import CollectionState
from .RuleLogic import state_has_at_least

location_rule_data_list: List[Callable[[CollectionState, int], bool]] = [
    lambda state, player:
    True,  # Rule 0
    lambda state, player:
    state.has("Eradia", player, 100),  # Rule 1
    lambda state, player:
    state.has("Tablet", player, 3),  # Rule 2
    lambda state, player:
    state.has("Tablet", player, 2),  # Rule 3
    lambda state, player:
    (state.has("Eradia", player, 100) and
     state.has("MQ4", player, 3)),  # Rule 4
    lambda state, player:
    (state.has("Arithmometer", player) and
     state.has("Eradia", player, 100)),  # Rule 5
    lambda state, player:
    (state.has("Loupe", player) and
     state.has("Eradia", player, 100)),  # Rule 6
    lambda state, player:
    (state.has("Eradia", player, 100) and
     state.has("MQ4", player)),  # Rule 7
    lambda state, player:
    (state.has("Monster Flesh", player) and
     state.has("Eradia", player, 700) and
     state.has("MQ4", player, 3)),  # Rule 8
    lambda state, player:
    (state.has("Tablet", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ4", player, 4)),  # Rule 9
    lambda state, player:
    state.has("Eradia", player, 700),  # Rule 10
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("Crux Base", player) and
     state.has("Crux Tip", player) and
     state.has("Crux Body", player) and
     state.has("Eradia", player, 100)),  # Rule 11
    lambda state, player:
    state.has("Eradia", player, 200),  # Rule 12
    lambda state, player:
    (state.has("Supply Sphere Password", player) and
     state.has("Eradia", player, 200)),  # Rule 13
    lambda state, player:
    state.has("Eradia", player, 300),  # Rule 14
    lambda state, player:
    (state.has("Thunderclap Cap", player) and
     state.has("Shaolong Gui Shell", player) and
     state.has("Mandragora Root", player) and
     state.has("Eradia", player, 200)),  # Rule 15
    lambda state, player:
    ((state.has("Green Carbuncle Doll", player) or
      state.has("Red Carbuncle Doll", player)) and
      state.has("Eradia", player, 200)),  # Rule 16
    lambda state, player:
    (state.has("Eradia", player, 200) and
     state.has("MQ1", player, 4)),  # Rule 17
    lambda state, player:
    (state.has("Spectral Elixir", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ1", player, 2)),  # Rule 18
    lambda state, player:
    (state.has("Supply Sphere Password", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ1", player, 2)),  # Rule 19
    lambda state, player:
    (state.has("Cursed Dragon Claw", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ1", player, 2)),  # Rule 20
    lambda state, player:
    (state.has("Eradia", player, 200) and
     state.has("MQ1", player, 2)),  # Rule 21
    lambda state, player:
    (state.has("Rubber Ball", player) and
     state.has("Eradia", player, 100) and
     state.has("MQ1", player, 5)),  # Rule 22
    lambda state, player:
    (state.has("Rubber Ball", player) and
     state.has("Eradia", player, 100)),  # Rule 23
    lambda state, player:
    (state.has("Eradia", player, 600) and
     state.has("MQ1", player, 2)),  # Rule 24
    lambda state, player:
    (state.has("Eradia", player, 200) and
     state.has("MQ1", player, 5)),  # Rule 25
    lambda state, player:
    (state.has("Eradia", player, 400) and
     state.has("MQ1", player, 5)),  # Rule 26
    lambda state, player:
    (state.has("Quill Pen", player) and
     state.has("Eradia", player, 700) and
     state.has("MQ1", player, 4)),  # Rule 27
    lambda state, player:
    (state.has("Eradia", player, 300) and
     state.has("MQ1", player, 5)),  # Rule 28
    lambda state, player:
    (state.has("Phantom Rose", player) and
     state.has("Eradia", player, 300) and
     state.has("MQ1", player, 5)),  # Rule 29
    lambda state, player:
    (state.has("Eradia", player, 800) and
     state.has("MQ1", player, 5)),  # Rule 30
    lambda state, player:
    state.has("Eradia", player, 500),  # Rule 31
    lambda state, player:
    state.has("Gysahl Greens", player),  # Rule 32
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 300)),  # Rule 33
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ3", player)),  # Rule 34
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 300) and
     state.has("MQ3", player)),  # Rule 35
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ3", player, 2)),  # Rule 36
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100) and
     state.has("MQ3", player)),  # Rule 37
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Data Recorder", player) and
     state.has("Eradia", player, 300) and
     state.has("MQ3", player, 3)),  # Rule 38
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 400) and
     state.has("MQ3", player)),  # Rule 39
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Aryas Apple", player, 2) and
     state.has("Eradia", player, 200) and
     state.has("MQ3", player, 2)),  # Rule 40
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Fragment of Mischief", player) and
     state.has("Fragment of Radiance", player) and
     state.has("Fragment of Smiles", player) and
     state.has("Fragment of Courage", player) and
     state.has("Fragment of Kindness", player) and
     state.has("Eradia", player, 200)),  # Rule 41
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Goddess Glyphs", player) and
     state.has("Chaos Glyphs", player) and
     state.has("Plate Metal Fragment", player) and
     state.has("Silvered Metal Fragment", player) and
     state.has("Golden Metal Fragment", player) and
     state.has("MQ3", player, 3)),  # Rule 42
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 400) and
     state.has("MQ3", player, 4)),  # Rule 43
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100) and
     state.has("MQ3", player, 3)),  # Rule 44
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200)),  # Rule 45
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ3", player, 3)),  # Rule 46
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Goddess Glyphs", player) and
     state.has("Chaos Glyphs", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ3", player, 3)),  # Rule 47
    lambda state, player:
    (state.has("ID Card", player) and
     state.has("Sneaking-In Special Ticket", player)),  # Rule 48
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 400)),  # Rule 49
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200)),  # Rule 50
    lambda state, player:
    state.has("Musical Treasure Sphere Key", player),  # Rule 51
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Eradia", player, 200)),  # Rule 52
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Eradia", player, 300)),  # Rule 53
    lambda state, player:
    (state.has("ID Card", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200)),  # Rule 54
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ2", player, 2)),  # Rule 55
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 400) and
     state.has("MQ2", player, 4)),  # Rule 56
    lambda state, player:
    (state.has("Music Satchel", player) and
     state.has("Eradia", player, 200)),  # Rule 57
    lambda state, player:
    (state.has("Father's Letter", player) and
     state.has("Eradia", player, 200)),  # Rule 58
    lambda state, player:
    (state.has("Civet Musk", player) and
     state.has("Gordon Gourmet's Recipe", player) and
     state.has("Steak a la Civet", player) and
     state.has("Eradia", player, 300)),  # Rule 59
    lambda state, player:
    (state.has("Nostalgic Score: Chorus", player) and
     state.has("Nostalgic Score: Refrain", player) and
     state.has("Nostalgic Score: Coda", player) and
     state.has("Eradia", player, 200)),  # Rule 60
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Eradia", player, 300) and
     state.has("MQ2", player, 2)),  # Rule 61
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Eradia", player, 300) and
     state.has("MQ2", player, 3)),  # Rule 62
    lambda state, player:
    state.has("Civet Musk", player),  # Rule 63
    lambda state, player:
    (state.has("Civet Musk", player) and
     state.has("Gordon Gourmet's Recipe", player) and
     state.has("Eradia", player, 200)),  # Rule 64
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 300)),  # Rule 65
    lambda state, player:
    state.has("Eradia", player, 400),  # Rule 66
    lambda state, player:
    state.has("Eradia", player, 600),  # Rule 67
    lambda state, player:
    state.has("Eradia", player, 800),  # Rule 68
    lambda state, player:
    state.has("Eradia", player, 900),  # Rule 69
    lambda state, player:
    state.has("Eradia", player, 1000),  # Rule 70
    lambda state, player:
    state.has("Eradia", player, 1100),  # Rule 71
    lambda state, player:
    state.has("Eradia", player, 1200),  # Rule 72
    lambda state, player:
    state.has("Eradia", player, 1300),  # Rule 73
    lambda state, player:
    state.has("Eradia", player, 1400),  # Rule 74
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("Crux Base", player) and
     state.has("Crux Tip", player) and
     state.has("Crux Body", player) and
     state.has("Eradia", player, 100) and
     state.has("MQ4", player, 6)),  # Rule 75
    lambda state, player:
    (state.has("Eradia", player, 100) and
     state.has("MQ1", player)),  # Rule 76
    lambda state, player:
    (state.has("Proof of Legendary Title", player) and
     state.has("Eradia", player, 300)),  # Rule 77
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 400)),  # Rule 78
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 500)),  # Rule 79
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 300) and
     state.has("MQ2", player, 4)),  # Rule 80
    lambda state, player:
    (state.has("Jade Hair Comb", player) and
     state.has("Bronze Pocket Watch", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ2", player)),  # Rule 81
    lambda state, player:
    (state.has("Chocobo Girl's Phone No.", player) and
     state.has("ID Card", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ2", player, 3)),  # Rule 82
    lambda state, player:
    (state.has("Beloved's Gift", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ5", player)),  # Rule 83
    lambda state, player:
    (state.has("Key to the Sand Gate", player) and
     state.has("Key to the Green Gate", player) and
     state.has("Eradia", player, 1100)),  # Rule 84
    lambda state, player:
    (state.has("Bandit's Bloodseal", player) and
     state.has("Oath of the Merchants Guild", player) and
     state.has("Eradia", player, 1100)),  # Rule 85
    lambda state, player:
    (state.has("Proof of Courage", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ1", player, 5)),  # Rule 86
    lambda state, player:
    (state.has("Violet Amulet", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ1", player, 5)),  # Rule 87
    lambda state, player:
    (state.has("Lapis Lazuli", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ2", player, 4)),  # Rule 88
    lambda state, player:
    (state.has("Power Booster", player) and
     state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Eradia", player, 300) and
     state.has("MQ2", player, 2)),  # Rule 89
    lambda state, player:
    (state.has("Moogle Dust", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100) and
     state.has("MQ3", player, 2)),  # Rule 90
    lambda state, player:
    (state.has("Old-Fashioned Photo Frame", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100) and
     state.has("MQ3", player, 2)),  # Rule 91
    lambda state, player:
    (state.has("Etro's Forbidden Tome", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 200) and
     state.has("MQ3", player, 4)),  # Rule 92
    lambda state, player:
    (state.has("Broken Gyroscope", player) and
     state.has("Eradia", player, 200)),  # Rule 93
    lambda state, player:
    (state.has("Golden Scarab", player) and
     state.has("Tablet", player, 2) and
     state.has("Eradia", player, 200)),  # Rule 94
    lambda state, player:
    state.has("Seedhunter Membership Card", player),  # Rule 95
    lambda state, player:
    (state.has("Seedhunter Membership Card", player) and
     state.has("Moogle Fragment", player)),  # Rule 96
    lambda state, player:
    state.has("Loupe", player),  # Rule 97
    lambda state, player:
    (state.has("Spectral Elixir", player) and
     state.has("Eradia", player, 200)),  # Rule 98
    lambda state, player:
    (state.has("Cursed Dragon Claw", player) and
     state.has("Eradia", player, 200)),  # Rule 99
    lambda state, player:
    (state.has("Quill Pen", player) and
     state.has("Eradia", player, 500)),  # Rule 100
    lambda state, player:
    (state.has("Phantom Rose", player) and
     state.has("Eradia", player, 300)),  # Rule 101
    lambda state, player:
    (state.has("Monster Flesh", player) and
     state.has("Eradia", player, 700)),  # Rule 102
    lambda state, player:
    (state.has("Tablet", player) and
     state.has("Eradia", player, 200)),  # Rule 103
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100)),  # Rule 104
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Data Recorder", player) and
     state.has("Eradia", player, 300)),  # Rule 105
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Aryas Apple", player, 2) and
     state.has("Eradia", player, 200)),  # Rule 106
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Goddess Glyphs", player) and
     state.has("Chaos Glyphs", player) and
     state.has("Plate Metal Fragment", player) and
     state.has("Silvered Metal Fragment", player) and
     state.has("Golden Metal Fragment", player)),  # Rule 107
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Eradia", player, 300)),  # Rule 108
    lambda state, player:
    state.has("Sneaking-In Special Ticket", player),  # Rule 109
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player)),  # Rule 110
    lambda state, player:
    (state.has("MQ2", player) and
     state.has("Midnight Mauve", player)),  # Rule 111
    lambda state, player:
    state.has("MQ3", player, 2),  # Rule 112
    lambda state, player:
    state.has("Tablet", player),  # Rule 113
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("MQ3", player, 3)),  # Rule 114
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Eradia", player, 200)),  # Rule 115
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("Eradia", player, 100)),  # Rule 116
    lambda state, player:
    (state.has("Beloved's Gift", player) and
     state.has("Gysahl Greens", player) and
     state.has("Eradia", player, 100)),  # Rule 117
    lambda state, player:
    (state.has("Moogle Fragment", player) and
     state.has("Gysahl Greens", player) and
     state.has("Seedhunter Membership Card", player) and
     state.has("Eradia", player, 100)),  # Rule 118
]

location_rule_data_table: Dict[str, Callable[[CollectionState, int], bool]] = {
    "Golden Scarab Treasure": location_rule_data_list[0],
    "Oasis Lighthouse Treasure (1)": location_rule_data_list[0],
    "Grave of the Colossi Shrine Treasure": location_rule_data_list[0],
    "Giant's Sandbox Treasure (1)": location_rule_data_list[0],
    "Golden Chamber Lower Treasure": location_rule_data_list[0],
    "Giant's Sandbox Treasure (2)": location_rule_data_list[0],
    "Giant's Sandbox Treasure (3)": location_rule_data_list[0],
    "Giant's Sandbox Treasure (4)": location_rule_data_list[0],
    "Ruffian Outdoor Treasure": location_rule_data_list[0],
    "Dry Floodlands Treasure (1)": location_rule_data_list[0],
    "Oasis Lighthouse Treasure (2)": location_rule_data_list[0],
    "Oasis Lighthouse Treasure (3)": location_rule_data_list[0],
    "Atomos's Sand Treasure (1)": location_rule_data_list[0],
    "Grave of the Colossi Treasure (1)": location_rule_data_list[0],
    "Grave of the Colossi Treasure (2)": location_rule_data_list[0],
    "Grave of the Colossi Treasure (3)": location_rule_data_list[0],
    "Atomos's Sand Treasure (2)": location_rule_data_list[0],
    "Ruffian 2nd Floor Treasure": location_rule_data_list[0],
    "Temple Ruins Chamber of Dusk (Upper) Treasure": location_rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Upper) Treasure (1)": location_rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Upper) Treasure (2)": location_rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Upper) Treasure (3)": location_rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Lower) Treasure (1)": location_rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Lower) Treasure (2)": location_rule_data_list[0],
    "Temple Ruins Chamber of Plenilune (Lower) Treasure (3)": location_rule_data_list[0],
    "Temple Ruins Sacred Grove Treasure": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Treasure (1)": location_rule_data_list[0],
    "Dry Floodlands Shrine Treasure": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Treasure (1)": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Treasure (2)": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Treasure (3)": location_rule_data_list[0],
    "Temple Ruins Scorched Earth (Lower) Treasure": location_rule_data_list[0],
    "Temple Ruins Scorched Earth (Upper) Treasure (1)": location_rule_data_list[0],
    "Temple Ruins Scorched Earth (Upper) Treasure (2)": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Treasure (2)": location_rule_data_list[0],
    "Atomos's Sands Shrine Treasure": location_rule_data_list[0],
    "Giant's Sandbox Treasure (5)": location_rule_data_list[0],
    "Dry Floodlands Treasure (2)": location_rule_data_list[0],
    "Grave of the Colossi Shrine Tablet": location_rule_data_list[1],
    "Dry Floodlands Shrine Tablet": location_rule_data_list[1],
    "Atomos's Sands Shrine Tablet": location_rule_data_list[1],
    "Temple Ruins Mural Crux Base": location_rule_data_list[2],
    "Temple Ruins Mural Crux Body": location_rule_data_list[3],
    "Temple Ruins Mural Crux Tip": location_rule_data_list[3],
    "Temple Ruins Bhakti Reward": location_rule_data_list[1],
    "Grave of the Colossi Pilgrim's Crux": location_rule_data_list[0],
    "Temple Ruins Scorched Earth Pilgrim's Crux (1)": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (1)": location_rule_data_list[0],
    "Temple Ruins Scorched Earth Pilgrim's Crux (2)": location_rule_data_list[0],
    "Dry Floodlands Pilgrim's Crux": location_rule_data_list[0],
    "Atomos's Sands Pilgrim's Crux": location_rule_data_list[0],
    "Giant's Sandbox Pilgrim's Crux": location_rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (1)": location_rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (2)": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (1)": location_rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (3)": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (2)": location_rule_data_list[0],
    "Temple Ruins Sacred Grove Pilgrim's Crux (4)": location_rule_data_list[0],
    "Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (2)": location_rule_data_list[0],
    "Atomos's Sands Loupe": location_rule_data_list[0],
    "The Life of a Machine Quest (1)": location_rule_data_list[4],
    "The Life of a Machine Quest (2)": location_rule_data_list[4],
    "Old Rivals Quest (1)": location_rule_data_list[5],
    "Old Rivals Quest (2)": location_rule_data_list[5],
    "His Wife's Dream Quest (1)": location_rule_data_list[5],
    "His Wife's Dream Quest (2)": location_rule_data_list[5],
    "Tool of the Trade Quest (1)": location_rule_data_list[6],
    "Tool of the Trade Quest (2)": location_rule_data_list[6],
    "Adonis's Audition Quest (1)": location_rule_data_list[7],
    "Adonis's Audition Quest (2)": location_rule_data_list[7],
    "What Rough Beast Slouches Quest (1)": location_rule_data_list[8],
    "What Rough Beast Slouches Quest (2)": location_rule_data_list[8],
    "Skeletons In The Closet Quest (1)": location_rule_data_list[9],
    "Skeletons In The Closet Quest (2)": location_rule_data_list[9],
    "Last One Standing Quest (1)": location_rule_data_list[10],
    "Last One Standing Quest (2)": location_rule_data_list[10],
    "Last One Standing Quest (3)": location_rule_data_list[10],
    "What Rough Beast Slouches Libra Notes": location_rule_data_list[0],
    "Dead Dunes Boss Drop": location_rule_data_list[11],
    "Aeronite Missable Drop": location_rule_data_list[10],
    "Cathedral Proof Of Courage": location_rule_data_list[12],
    "Pilgrim's Passage Violet Amulet Treasure": location_rule_data_list[0],
    "North Station Plaza Treasure": location_rule_data_list[0],
    "The Avenue Treasure": location_rule_data_list[0],
    "Gallery Steps Treasure": location_rule_data_list[0],
    "2nd Ave Treasure": location_rule_data_list[0],
    "Pilgrim's Passage (Grassy) Treasure": location_rule_data_list[0],
    "Old Theater Platform Treasure": location_rule_data_list[0],
    "The Warren Mangled Hill Treasure": location_rule_data_list[0],
    "South Station (Supply Sphere) Treasure": location_rule_data_list[13],
    "Warehouse District (Supply Sphere) Treasure": location_rule_data_list[13],
    "Residences (Supply Sphere) Treasure": location_rule_data_list[13],
    "Forsaken Graveyard Treasure (1)": location_rule_data_list[12],
    "Den Of Shadows Treasure (1)": location_rule_data_list[12],
    "Luxerion After 1st Phone (1)": location_rule_data_list[0],
    "Den Of Shadows Treasure (2)": location_rule_data_list[12],
    "Luxerion After 1st Phone (2)": location_rule_data_list[0],
    "Luxerion After 1st Phone (3)": location_rule_data_list[0],
    "Luxerion Marketplace Treasure": location_rule_data_list[0],
    "Forsaken Graveyard Treasure (2)": location_rule_data_list[12],
    "1st Ave Rubber Ball": location_rule_data_list[1],
    "Marketplace Doll": location_rule_data_list[12],
    "North Station Plaza Doll": location_rule_data_list[12],
    "Warehouse District Thunderclap Cap": location_rule_data_list[0],
    "Luxerion Proof of Legendary Title": location_rule_data_list[12],
    "Luxerion Ghost Phantom Rose": location_rule_data_list[14],
    "Luxerion Marketplace Pen": location_rule_data_list[14],
    "Baird Seedhunter Membership Card": location_rule_data_list[0],
    "Virgil Supply Sphere Password": location_rule_data_list[12],
    "Buy Shaolong Gui Shell": location_rule_data_list[0],
    "Buy Mandragora Root": location_rule_data_list[1],
    "Chocobo Emporium Spectral Elixir": location_rule_data_list[15],
    "The Things She Lost Quest (1)": location_rule_data_list[16],
    "The Things She Lost Quest (2)": location_rule_data_list[16],
    "Where Are You, Holmes? Quest (1)": location_rule_data_list[1],
    "Where Are You, Holmes? Quest (2)": location_rule_data_list[1],
    "Where Are You, Holmes? Quest (3)": location_rule_data_list[1],
    "Like Clockwork Quest (1)": location_rule_data_list[17],
    "Like Clockwork Quest (2)": location_rule_data_list[17],
    "Dying Wish Quest (1)": location_rule_data_list[18],
    "Dying Wish Quest (2)": location_rule_data_list[18],
    "Suspicious Spheres Quest (1)": location_rule_data_list[19],
    "Suspicious Spheres Quest (2)": location_rule_data_list[19],
    "Born From Chaos Quest (1)": location_rule_data_list[20],
    "Born From Chaos Quest (2)": location_rule_data_list[20],
    "Born From Chaos Quest (3)": location_rule_data_list[20],
    "Born From Chaos Quest (4)": location_rule_data_list[20],
    "Soul Seeds Quest (1)": location_rule_data_list[21],
    "Soul Seeds Quest (2)": location_rule_data_list[21],
    "Faster Than Lightning Quest (1)": location_rule_data_list[21],
    "Faster Than Lightning Quest (2)": location_rule_data_list[21],
    "Treasured Ball Quest (1)": location_rule_data_list[22],
    "Treasured Ball Quest (2)": location_rule_data_list[22],
    "Talbot's Gratitude": location_rule_data_list[23],
    "The Angel's Tears Quest (1)": location_rule_data_list[24],
    "The Angel's Tears Quest (2)": location_rule_data_list[24],
    "The Saint's Stone Quest (1)": location_rule_data_list[25],
    "The Saint's Stone Quest (2)": location_rule_data_list[25],
    "The Saint's Stone Quest (3)": location_rule_data_list[25],
    "Aremiah Service Entrance Key": location_rule_data_list[12],
    "Whither Faith Quest (1)": location_rule_data_list[1],
    "Whither Faith Quest (2)": location_rule_data_list[1],
    "The Avid Reader Quest (1)": location_rule_data_list[26],
    "The Avid Reader Quest (2)": location_rule_data_list[26],
    "Buried Passion Quest (1)": location_rule_data_list[27],
    "Buried Passion Quest (2)": location_rule_data_list[27],
    "The Girl Who Cried Wolf Quest (1)": location_rule_data_list[28],
    "The Girl Who Cried Wolf Quest (2)": location_rule_data_list[28],
    "Stuck in a Gem Quest (1)": location_rule_data_list[12],
    "Stuck in a Gem Quest (2)": location_rule_data_list[12],
    "Get the Girl Quest (1)": location_rule_data_list[25],
    "Get the Girl Quest (2)": location_rule_data_list[25],
    "A Rose By Any Other Name Quest (1)": location_rule_data_list[29],
    "A Rose By Any Other Name Quest (2)": location_rule_data_list[29],
    "A Rose By Any Other Name Quest (3)": location_rule_data_list[29],
    "A Rose By Any Other Name Quest (4)": location_rule_data_list[29],
    "Voices from the Grave Quest (1)": location_rule_data_list[28],
    "Voices from the Grave Quest (2)": location_rule_data_list[28],
    "To Save the Sinless Quest (1)": location_rule_data_list[30],
    "To Save the Sinless Quest (2)": location_rule_data_list[30],
    "Replace Chronostasis": location_rule_data_list[1],
    "Luxerion Boss Drop": location_rule_data_list[12],
    "Luxerion Boss+ Only Missable Drop": location_rule_data_list[31],
    "Moogle Village Moogle Dust Treasure": location_rule_data_list[0],
    "Research Camp Photo Frame Treasure": location_rule_data_list[0],
    "Poltae Etro's Forbidden Tome": location_rule_data_list[0],
    "Eremite Plains Broken Gyroscope Treasure": location_rule_data_list[32],
    "Aryas Village Treasure (1)": location_rule_data_list[0],
    "Jagd Woods Treasure": location_rule_data_list[32],
    "The Grasslands Treasure (1)": location_rule_data_list[32],
    "Poltae Treasure (1)": location_rule_data_list[32],
    "Canopus Farms Treasure": location_rule_data_list[0],
    "Rocky Crag Treasure (1)": location_rule_data_list[32],
    "The Grasslands Treasure (2)": location_rule_data_list[32],
    "Aryas Village Treasure (2)": location_rule_data_list[0],
    "The Grasslands Treasure (3)": location_rule_data_list[32],
    "Eremite Plains Treasure (1)": location_rule_data_list[32],
    "Eremite Plains Treasure (2)": location_rule_data_list[32],
    "Moogle Village Treasure": location_rule_data_list[32],
    "City of Ruins Treasure": location_rule_data_list[32],
    "Rocky Crag Treasure (2)": location_rule_data_list[32],
    "Rocky Crag Treasure (3)": location_rule_data_list[32],
    "Aryas Village Treasure (3)": location_rule_data_list[32],
    "Poltae Treasure (2)": location_rule_data_list[0],
    "Eremite Plains Crash Site Fragment": location_rule_data_list[32],
    "Goddess Temple Treasure (1)": location_rule_data_list[33],
    "Goddess Temple Treasure (2)": location_rule_data_list[33],
    "Goddess Temple Treasure (3)": location_rule_data_list[33],
    "Goddess Temple Treasure (4)": location_rule_data_list[33],
    "Goddess Temple Treasure (5)": location_rule_data_list[33],
    "Goddess Temple Treasure (6)": location_rule_data_list[33],
    "Goddess Temple Treasure (7)": location_rule_data_list[33],
    "Goddess Temple Treasure (8)": location_rule_data_list[33],
    "Goddess Temple Treasure (9)": location_rule_data_list[33],
    "Dr Gysahl's Gysahl Greens": location_rule_data_list[0],
    "Aryas Village Beloved's Gift Treasure": location_rule_data_list[0],
    "Sarala Vegatable Seeds": location_rule_data_list[32],
    "A Father's Request Quest (1)": location_rule_data_list[34],
    "A Father's Request Quest (2)": location_rule_data_list[34],
    "The Hunter's Challenge Quest (1)": location_rule_data_list[35],
    "The Hunter's Challenge Quest (2)": location_rule_data_list[35],
    "The Hunter's Challenge Quest (3)": location_rule_data_list[35],
    "A Final Cure Quest (1)": location_rule_data_list[34],
    "A Final Cure Quest (2)": location_rule_data_list[34],
    "A Final Cure Quest (3)": location_rule_data_list[34],
    "Fuzzy Search Quest (1)": location_rule_data_list[12],
    "Fuzzy Search Quest (2)": location_rule_data_list[12],
    "Fuzzy Search Quest (3)": location_rule_data_list[12],
    "Round 'em Up Quest (1)": location_rule_data_list[36],
    "Round 'em Up Quest (2)": location_rule_data_list[36],
    "Chocobo Cheer Quest (1)": location_rule_data_list[36],
    "Chocobo Cheer Quest (2)": location_rule_data_list[36],
    "Chocobo Cheer Quest (3)": location_rule_data_list[36],
    "Peace and Quiet, Kupo Quest (1)": location_rule_data_list[1],
    "Peace and Quiet, Kupo Quest (2)": location_rule_data_list[1],
    "Peace and Quiet, Kupo Quest (3)": location_rule_data_list[1],
    "Saving an Angel Quest (1)": location_rule_data_list[37],
    "Saving an Angel Quest (2)": location_rule_data_list[37],
    "Omega Point Quest (1)": location_rule_data_list[38],
    "Omega Point Quest (2)": location_rule_data_list[38],
    "The Old Man and the Field Quest (1)": location_rule_data_list[35],
    "The Old Man and the Field Quest (2)": location_rule_data_list[35],
    "Land of our Forebears Quest (1)": location_rule_data_list[39],
    "Land of our Forebears Quest (2)": location_rule_data_list[39],
    "A Taste of the Past Quest (1)": location_rule_data_list[40],
    "A Taste of the Past Quest (2)": location_rule_data_list[40],
    "A Taste of the Past Quest (3)": location_rule_data_list[40],
    "Dog, Doctor and Assistant Quest (1)": location_rule_data_list[36],
    "Dog, Doctor and Assistant Quest (2)": location_rule_data_list[36],
    "Main Quest 5 (1)": location_rule_data_list[41],
    "Main Quest 5 (2)": location_rule_data_list[41],
    "Main Quest 5 (3)": location_rule_data_list[41],
    "The Right Stuff Quest (1)": location_rule_data_list[34],
    "The Right Stuff Quest (2)": location_rule_data_list[34],
    "The Secret Lives of Sheep Quest (1)": location_rule_data_list[33],
    "The Secret Lives of Sheep Quest (2)": location_rule_data_list[33],
    "Where Are You, Moogle? Quest (1)": location_rule_data_list[1],
    "Where Are You, Moogle? Quest (2)": location_rule_data_list[1],
    "Where Are You, Moogle? Quest (3)": location_rule_data_list[1],
    "Mercy of a Goddess Quest (1)": location_rule_data_list[33],
    "Mercy of a Goddess Quest (2)": location_rule_data_list[33],
    "The Grail of Valhalla Quest (1)": location_rule_data_list[42],
    "The Grail of Valhalla Quest (2)": location_rule_data_list[42],
    "The Grail of Valhalla Quest (3)": location_rule_data_list[42],
    "To Live in Chaos Quest (1)": location_rule_data_list[43],
    "To Live in Chaos Quest (2)": location_rule_data_list[43],
    "To Live in Chaos Quest (3)": location_rule_data_list[43],
    "Killing Time Quest (1)": location_rule_data_list[44],
    "Killing Time Quest (2)": location_rule_data_list[44],
    "Matchmaker Quest (1)": location_rule_data_list[45],
    "Matchmaker Quest (2)": location_rule_data_list[45],
    "Mother and Daughter Quest (1)": location_rule_data_list[45],
    "Mother and Daughter Quest (2)": location_rule_data_list[45],
    "The Secret Lives of Sheep Mystery Egg": location_rule_data_list[33],
    "Goddess Temple Goddess Glyphs": location_rule_data_list[46],
    "Goddess Temple Chaos Glyphs": location_rule_data_list[46],
    "Poltae Plate Metal Fragment": location_rule_data_list[47],
    "Poltae Silvered Metal Fragment": location_rule_data_list[47],
    "Poltae Gold Metal Fragment": location_rule_data_list[47],
    "Research Camp Data Recorder": location_rule_data_list[45],
    "Aryas Village Apple (1)": location_rule_data_list[45],
    "Aryas Village Apple (2)": location_rule_data_list[45],
    "Aryas Village Apple (3)": location_rule_data_list[45],
    "Wildlands Boss Drop": location_rule_data_list[33],
    "Reveler's Quarter Lapis Lazuli Treasure": location_rule_data_list[0],
    "Industrial Area Power Booster": location_rule_data_list[48],
    "Tunnel Oath of the Merchants Guild Treasure": location_rule_data_list[0],
    "Industrial Area Jade Hair Comb": location_rule_data_list[49],
    "Industrial Area Bronze Pocket Watch": location_rule_data_list[50],
    "Chocobo Girl Poster": location_rule_data_list[0],
    "Glutton's Quarter Treasure (1)": location_rule_data_list[0],
    "Aromatic Market Treasure": location_rule_data_list[0],
    "Central Ave Treasure": location_rule_data_list[0],
    "Coliseum Square Treasure": location_rule_data_list[0],
    "Tour Guide Sneaking-In Special Ticket": location_rule_data_list[0],
    "Warehouse District Id Card": location_rule_data_list[50],
    "Coliseum Square (Musical) Treasure": location_rule_data_list[51],
    "Cactuar Statue (Musical) Treasure": location_rule_data_list[51],
    "Station (Musical) Treasure": location_rule_data_list[51],
    "Cactuar Statue Treasure": location_rule_data_list[0],
    "Reveler's Quarter Treasure (1)": location_rule_data_list[0],
    "Augur's Quarter Treasure (1)": location_rule_data_list[52],
    "Patron's Palace Treasure (1)": location_rule_data_list[53],
    "Hawker's Row Treasure": location_rule_data_list[0],
    "Augur's Quarter Treasure (2)": location_rule_data_list[52],
    "Warehouse District Treasure": location_rule_data_list[50],
    "Augur's Quarter Treasure (3)": location_rule_data_list[54],
    "Supply Line Treasure": location_rule_data_list[50],
    "Industrial Area Treasure": location_rule_data_list[50],
    "Lower City Treasure": location_rule_data_list[0],
    "Glutton's Quarter Treasure (2)": location_rule_data_list[0],
    "Reveler's Quarter Treasure (2)": location_rule_data_list[0],
    "Patron's Palace Treasure (2)": location_rule_data_list[53],
    "Patron's Palace Treasure (3)": location_rule_data_list[53],
    "Patron's Palace Treasure (4)": location_rule_data_list[53],
    "Patron's Palace Treasure (5)": location_rule_data_list[53],
    "Slaughterhouse Special Fragment of Courage": location_rule_data_list[45],
    "Slaughterhouse (1)": location_rule_data_list[0],
    "Slaughterhouse (2)": location_rule_data_list[0],
    "Slaughterhouse (3)": location_rule_data_list[0],
    "Slaughterhouse (4)": location_rule_data_list[0],
    "Slaughterhouse (5)": location_rule_data_list[0],
    "Slaughterhouse (6)": location_rule_data_list[0],
    "Slaughterhouse (7)": location_rule_data_list[0],
    "Slaughterhouse (8)": location_rule_data_list[0],
    "Slaughterhouse (9)": location_rule_data_list[0],
    "Slaughterhouse (10)": location_rule_data_list[0],
    "The Fighting Actress Slaughterhouse (1)": location_rule_data_list[55],
    "The Fighting Actress Slaughterhouse (2)": location_rule_data_list[55],
    "The Fighting Actress Slaughterhouse (3)": location_rule_data_list[55],
    "The Fighting Actress Slaughterhouse (4)": location_rule_data_list[55],
    "Tanbam's Taboo Slaughterhouse": location_rule_data_list[56],
    "Chocobo Girl Miqo'te Dress": location_rule_data_list[0],
    "Director Femme Fetale": location_rule_data_list[53],
    "Fireworks in a Bottle Quest (1)": location_rule_data_list[55],
    "Fireworks in a Bottle Quest (2)": location_rule_data_list[55],
    "The Fighting Actress Quest (1)": location_rule_data_list[55],
    "The Fighting Actress Quest (2)": location_rule_data_list[55],
    "Songless Diva Quest (1)": location_rule_data_list[57],
    "Songless Diva Quest (2)": location_rule_data_list[57],
    "Stolen Things Quest (1)": location_rule_data_list[58],
    "Stolen Things Quest (2)": location_rule_data_list[58],
    "Fireworks for a Steal Quest (1)": location_rule_data_list[55],
    "Fireworks for a Steal Quest (2)": location_rule_data_list[55],
    "A Testing Proposition Quest (1)": location_rule_data_list[31],
    "A Testing Proposition Quest (2)": location_rule_data_list[31],
    "Last Date Quest (1)": location_rule_data_list[56],
    "Last Date Quest (2)": location_rule_data_list[56],
    "Free Will Quest (1)": location_rule_data_list[14],
    "Free Will Quest (2)": location_rule_data_list[14],
    "Free Will Quest (3)": location_rule_data_list[14],
    "Friends Forever Quest (1)": location_rule_data_list[56],
    "Friends Forever Quest (2)": location_rule_data_list[56],
    "Friends Forever Quest (3)": location_rule_data_list[56],
    "Family Food Quest (1)": location_rule_data_list[59],
    "Family Food Quest (2)": location_rule_data_list[59],
    "Tanbam's Taboo Quest (1)": location_rule_data_list[56],
    "Tanbam's Taboo Quest (2)": location_rule_data_list[56],
    "Play It for Me Quest (1)": location_rule_data_list[60],
    "Play It for Me Quest (2)": location_rule_data_list[60],
    "Adoring Adornments Quest (1)": location_rule_data_list[61],
    "Adoring Adornments Quest (2)": location_rule_data_list[61],
    "Adoring Candice Quest (1)": location_rule_data_list[56],
    "Adoring Candice Quest (2)": location_rule_data_list[56],
    "Adoring Candice Quest (3)": location_rule_data_list[56],
    "Death Safari Quest (1)": location_rule_data_list[61],
    "Death Safari Quest (2)": location_rule_data_list[61],
    "Death Safari Quest (3)": location_rule_data_list[61],
    "Death Safari Quest (4)": location_rule_data_list[61],
    "Death Safari Quest (5)": location_rule_data_list[61],
    "Death Game Quest (1)": location_rule_data_list[61],
    "Death Game Quest (2)": location_rule_data_list[61],
    "Death Game Quest (3)": location_rule_data_list[61],
    "Morris Musical Treasure Sphere Key": location_rule_data_list[12],
    "Patron's Palace Serah's Pendant": location_rule_data_list[62],
    "Gordon Gourmet's Recipe": location_rule_data_list[63],
    "Seedy Steak a la Civet": location_rule_data_list[64],
    "Gregory Father's Letter": location_rule_data_list[12],
    "Tanbam's Taboo Libra Notes": location_rule_data_list[56],
    "Yusnaan Boss Drop": location_rule_data_list[65],
    "Initial 3rd Garb (1)": location_rule_data_list[0],
    "Initial 3rd Garb (2)": location_rule_data_list[0],
    "Initial 3rd Garb (3)": location_rule_data_list[0],
    "Ark Day 1 (1)": location_rule_data_list[1],
    "Ark Day 1 (2)": location_rule_data_list[1],
    "Ark Day 1 (3)": location_rule_data_list[1],
    "Ark Day 1 (4)": location_rule_data_list[1],
    "Ark Day 1 (5)": location_rule_data_list[1],
    "Ark Day 2 (1)": location_rule_data_list[12],
    "Ark Day 2 (2)": location_rule_data_list[12],
    "Ark Day 2 (3)": location_rule_data_list[12],
    "Ark Day 3 (1)": location_rule_data_list[14],
    "Ark Day 4 (1)": location_rule_data_list[66],
    "Ark Day 4 (2)": location_rule_data_list[66],
    "Ark Day 5 (1)": location_rule_data_list[31],
    "Ark Day 6 (1)": location_rule_data_list[67],
    "Ark Day 7": location_rule_data_list[10],
    "Ark Day 8": location_rule_data_list[68],
    "Ark Day 9": location_rule_data_list[69],
    "Ark Day 10": location_rule_data_list[70],
    "Ark Day 11": location_rule_data_list[71],
    "Ark Day 12": location_rule_data_list[72],
    "Ark Final Day (1)": location_rule_data_list[73],
    "Ark Final Day (2)": location_rule_data_list[73],
    "Ark Final Day (3)": location_rule_data_list[73],
    "Ark Extra Day": location_rule_data_list[74],
    "Replace Curaga": location_rule_data_list[0],
    "Replace Teleport": location_rule_data_list[0],
    "Replace Escape": location_rule_data_list[0],
    "Flower in the Sands CoP Quest (1)": location_rule_data_list[1],
    "Flower in the Sands CoP Quest (2)": location_rule_data_list[1],
    "Biologically Speaking CoP Quest (1)": location_rule_data_list[1],
    "Biologically Speaking CoP Quest (2)": location_rule_data_list[1],
    "The Real Client CoP Quest (1)": location_rule_data_list[66],
    "The Real Client CoP Quest (2)": location_rule_data_list[66],
    "The Real Client CoP Quest (3)": location_rule_data_list[66],
    "For My Child CoP Quest (1)": location_rule_data_list[14],
    "For My Child CoP Quest (2)": location_rule_data_list[14],
    "For My Child CoP Quest (3)": location_rule_data_list[14],
    "Bandits' New Weapon CoP Quest (1)": location_rule_data_list[66],
    "Bandits' New Weapon CoP Quest (2)": location_rule_data_list[66],
    "Bandits' New Weapon CoP Quest (3)": location_rule_data_list[66],
    "Banned Goods CoP Quest (1)": location_rule_data_list[1],
    "Banned Goods CoP Quest (2)": location_rule_data_list[1],
    "Banned Goods CoP Quest (3)": location_rule_data_list[1],
    "Climbing The Ranks I CoP Quest (1)": location_rule_data_list[14],
    "Climbing The Ranks I CoP Quest (2)": location_rule_data_list[14],
    "Miracle Vintage CoP Quest (1)": location_rule_data_list[66],
    "Miracle Vintage CoP Quest (2)": location_rule_data_list[66],
    "Miracle Vintage CoP Quest (3)": location_rule_data_list[66],
    "Climbing The Ranks II CoP Quest (1)": location_rule_data_list[14],
    "Climbing The Ranks II CoP Quest (2)": location_rule_data_list[14],
    "Heightened Security CoP Quest (1)": location_rule_data_list[66],
    "Heightened Security CoP Quest (2)": location_rule_data_list[66],
    "Heightened Security CoP Quest (3)": location_rule_data_list[66],
    "Desert Cleanup CoP Quest (1)": location_rule_data_list[1],
    "Desert Cleanup CoP Quest (2)": location_rule_data_list[1],
    "Desert Cleanup CoP Quest (3)": location_rule_data_list[1],
    "A Treasure for a God CoP Quest (1)": location_rule_data_list[75],
    "A Treasure for a God CoP Quest (2)": location_rule_data_list[75],
    "Lucky Charm CoP Quest (1)": location_rule_data_list[1],
    "Lucky Charm CoP Quest (2)": location_rule_data_list[1],
    "Supply and Demand CoP Quest (1)": location_rule_data_list[14],
    "Supply and Demand CoP Quest (2)": location_rule_data_list[14],
    "Supply and Demand CoP Quest (3)": location_rule_data_list[14],
    "A New Application CoP Quest (1)": location_rule_data_list[59],
    "A New Application CoP Quest (2)": location_rule_data_list[59],
    "A New Application CoP Quest (3)": location_rule_data_list[59],
    "Pride And Greed I CoP Quest (1)": location_rule_data_list[14],
    "Pride And Greed I CoP Quest (2)": location_rule_data_list[14],
    "Pride And Greed I CoP Quest (3)": location_rule_data_list[14],
    "Pride And Greed II CoP Quest (1)": location_rule_data_list[10],
    "Pride And Greed II CoP Quest (2)": location_rule_data_list[10],
    "Pride And Greed II CoP Quest (3)": location_rule_data_list[10],
    "Pride And Greed III CoP Quest (1)": location_rule_data_list[71],
    "Pride And Greed III CoP Quest (2)": location_rule_data_list[71],
    "Pride And Greed III CoP Quest (3)": location_rule_data_list[71],
    "Revenge Is Sweet CoP Quest (1)": location_rule_data_list[76],
    "Revenge Is Sweet CoP Quest (2)": location_rule_data_list[76],
    "Gift of Gratitude CoP Quest (1)": location_rule_data_list[76],
    "Gift of Gratitude CoP Quest (2)": location_rule_data_list[76],
    "Gift of Gratitude CoP Quest (3)": location_rule_data_list[76],
    "A Song for God CoP Quest (1)": location_rule_data_list[14],
    "A Song for God CoP Quest (2)": location_rule_data_list[14],
    "A Song for God CoP Quest (3)": location_rule_data_list[14],
    "Slay the Machine CoP Quest (1)": location_rule_data_list[14],
    "Slay the Machine CoP Quest (2)": location_rule_data_list[14],
    "Enchanted Brush CoP Quest (1)": location_rule_data_list[31],
    "Enchanted Brush CoP Quest (2)": location_rule_data_list[31],
    "Enchanted Brush CoP Quest (3)": location_rule_data_list[31],
    "Heretics' Beasts CoP Quest (1)": location_rule_data_list[31],
    "Heretics' Beasts CoP Quest (2)": location_rule_data_list[31],
    "Heretics' Beasts CoP Quest (3)": location_rule_data_list[31],
    "Grave of a Bounty Hunter CoP Quest (1)": location_rule_data_list[31],
    "Grave of a Bounty Hunter CoP Quest (2)": location_rule_data_list[31],
    "Grave of a Bounty Hunter CoP Quest (3)": location_rule_data_list[31],
    "Inventive Seamstress CoP Quest (1)": location_rule_data_list[76],
    "Inventive Seamstress CoP Quest (2)": location_rule_data_list[76],
    "Puppeteer's Lament CoP Quest (1)": location_rule_data_list[31],
    "Puppeteer's Lament CoP Quest (2)": location_rule_data_list[31],
    "Puppeteer's Lament CoP Quest (3)": location_rule_data_list[31],
    "Revenge has Teeth CoP Quest (1)": location_rule_data_list[31],
    "Revenge has Teeth CoP Quest (2)": location_rule_data_list[31],
    "Night Patrol CoP Quest (1)": location_rule_data_list[31],
    "Night Patrol CoP Quest (2)": location_rule_data_list[31],
    "Night Patrol CoP Quest (3)": location_rule_data_list[31],
    "Trapped CoP Quest (1)": location_rule_data_list[76],
    "Trapped CoP Quest (2)": location_rule_data_list[76],
    "Trapped CoP Quest (3)": location_rule_data_list[76],
    "Trapped CoP Quest (4)": location_rule_data_list[76],
    "Mythical Badge CoP Quest (1)": location_rule_data_list[77],
    "Mythical Badge CoP Quest (2)": location_rule_data_list[77],
    "Mythical Badge CoP Quest (3)": location_rule_data_list[77],
    "Sun Flower CoP Quest (1)": location_rule_data_list[1],
    "Sun Flower CoP Quest (2)": location_rule_data_list[1],
    "Moon Flower CoP Quest (1)": location_rule_data_list[1],
    "Moon Flower CoP Quest (2)": location_rule_data_list[1],
    "Moon Flower CoP Quest (3)": location_rule_data_list[1],
    "Secret of the Chocoborel CoP Quest (1)": location_rule_data_list[14],
    "Secret of the Chocoborel CoP Quest (2)": location_rule_data_list[14],
    "Secret of the Chocoborel CoP Quest (3)": location_rule_data_list[14],
    "Wildlands In Danger! CoP Quest (1)": location_rule_data_list[33],
    "Wildlands In Danger! CoP Quest (2)": location_rule_data_list[33],
    "Wildlands In Danger! CoP Quest (3)": location_rule_data_list[33],
    "Hunting the Hunter CoP Quest (1)": location_rule_data_list[14],
    "Hunting the Hunter CoP Quest (2)": location_rule_data_list[14],
    "Hunting the Hunter CoP Quest (3)": location_rule_data_list[14],
    "Forget Me Not CoP Quest (1)": location_rule_data_list[1],
    "Forget Me Not CoP Quest (2)": location_rule_data_list[1],
    "Forget Me Not CoP Quest (3)": location_rule_data_list[1],
    "A Word of Thanks CoP Quest (1)": location_rule_data_list[14],
    "A Word of Thanks CoP Quest (2)": location_rule_data_list[14],
    "A Word of Thanks CoP Quest (3)": location_rule_data_list[14],
    "Fresh Fertilizer CoP Quest (1)": location_rule_data_list[78],
    "Fresh Fertilizer CoP Quest (2)": location_rule_data_list[78],
    "Fresh Fertilizer CoP Quest (3)": location_rule_data_list[78],
    "For the Future CoP Quest (1)": location_rule_data_list[14],
    "For the Future CoP Quest (2)": location_rule_data_list[14],
    "For the Future CoP Quest (3)": location_rule_data_list[14],
    "Dumpling Cook-Off CoP Quest (1)": location_rule_data_list[14],
    "Dumpling Cook-Off CoP Quest (2)": location_rule_data_list[14],
    "Dumpling Cook-Off CoP Quest (3)": location_rule_data_list[14],
    "Brain Over Brawn CoP Quest (1)": location_rule_data_list[10],
    "Brain Over Brawn CoP Quest (2)": location_rule_data_list[10],
    "Brain Over Brawn CoP Quest (3)": location_rule_data_list[10],
    "Hunter's Challenge CoP Quest (1)": location_rule_data_list[14],
    "Hunter's Challenge CoP Quest (2)": location_rule_data_list[14],
    "Hunter's Challenge CoP Quest (3)": location_rule_data_list[14],
    "A Secret Wish CoP Quest (1)": location_rule_data_list[14],
    "A Secret Wish CoP Quest (2)": location_rule_data_list[14],
    "A Secret Wish CoP Quest (3)": location_rule_data_list[14],
    "Moghan's Plea CoP Quest (1)": location_rule_data_list[1],
    "Moghan's Plea CoP Quest (2)": location_rule_data_list[1],
    "Moghan's Plea CoP Quest (3)": location_rule_data_list[1],
    "What's in a Brew? CoP Quest (1)": location_rule_data_list[79],
    "What's in a Brew? CoP Quest (2)": location_rule_data_list[79],
    "What's in a Brew? CoP Quest (3)": location_rule_data_list[79],
    "What's in a Brew? CoP Quest (4)": location_rule_data_list[79],
    "A Prayer to a Goddess CoP Quest (1)": location_rule_data_list[10],
    "A Prayer to a Goddess CoP Quest (2)": location_rule_data_list[10],
    "A Prayer to a Goddess CoP Quest (3)": location_rule_data_list[10],
    "Gatekeeper's Curiosity CoP Quest (1)": location_rule_data_list[31],
    "Gatekeeper's Curiosity CoP Quest (2)": location_rule_data_list[31],
    "Echoes of a Drum CoP Quest (1)": location_rule_data_list[14],
    "Echoes of a Drum CoP Quest (2)": location_rule_data_list[14],
    "Echoes of a Drum CoP Quest (3)": location_rule_data_list[14],
    "A Voice From Below CoP Quest (1)": location_rule_data_list[14],
    "A Voice From Below CoP Quest (2)": location_rule_data_list[14],
    "A Voice From Below CoP Quest (3)": location_rule_data_list[14],
    "Chocobo Chow CoP Quest (1)": location_rule_data_list[45],
    "Chocobo Chow CoP Quest (2)": location_rule_data_list[45],
    "Chocobo Chow CoP Quest (3)": location_rule_data_list[45],
    "Sylkis Secrets CoP Quest (1)": location_rule_data_list[33],
    "Sylkis Secrets CoP Quest (2)": location_rule_data_list[33],
    "Sylkis Secrets CoP Quest (3)": location_rule_data_list[33],
    "Digging Mole CoP Quest (1)": location_rule_data_list[45],
    "Digging Mole CoP Quest (2)": location_rule_data_list[45],
    "Digging Mole CoP Quest (3)": location_rule_data_list[45],
    "Two Together CoP Quest (1)": location_rule_data_list[14],
    "Two Together CoP Quest (2)": location_rule_data_list[14],
    "Two Together CoP Quest (3)": location_rule_data_list[14],
    "Emergency Treatment CoP Quest (1)": location_rule_data_list[36],
    "Emergency Treatment CoP Quest (2)": location_rule_data_list[36],
    "Emergency Treatment CoP Quest (3)": location_rule_data_list[45],
    "Moogle Gourmand CoP Quest (1)": location_rule_data_list[45],
    "Moogle Gourmand CoP Quest (2)": location_rule_data_list[45],
    "Moogle Gourmand CoP Quest (3)": location_rule_data_list[45],
    "Secret Machine CoP Quest (1)": location_rule_data_list[1],
    "Secret Machine CoP Quest (2)": location_rule_data_list[1],
    "Soulful Horn CoP Quest (1)": location_rule_data_list[12],
    "Soulful Horn CoP Quest (2)": location_rule_data_list[12],
    "Soulful Horn CoP Quest (3)": location_rule_data_list[12],
    "A Dangerous Cocktail CoP Quest (1)": location_rule_data_list[14],
    "A Dangerous Cocktail CoP Quest (2)": location_rule_data_list[14],
    "Source of Inspiration CoP Quest (1)": location_rule_data_list[31],
    "Source of Inspiration CoP Quest (2)": location_rule_data_list[31],
    "Youth Potion CoP Quest (1)": location_rule_data_list[10],
    "Youth Potion CoP Quest (2)": location_rule_data_list[10],
    "Youth Potion CoP Quest (3)": location_rule_data_list[10],
    "Beast Summoner CoP Quest (1)": location_rule_data_list[31],
    "Beast Summoner CoP Quest (2)": location_rule_data_list[31],
    "Beast Summoner CoP Quest (3)": location_rule_data_list[31],
    "What Seekers Seek CoP Quest (1)": location_rule_data_list[10],
    "What Seekers Seek CoP Quest (2)": location_rule_data_list[10],
    "What Seekers Seek CoP Quest (3)": location_rule_data_list[10],
    "True Colors CoP Quest (1)": location_rule_data_list[31],
    "True Colors CoP Quest (2)": location_rule_data_list[31],
    "True Colors CoP Quest (3)": location_rule_data_list[31],
    "Ultimate Craving CoP Quest (1)": location_rule_data_list[10],
    "Ultimate Craving CoP Quest (2)": location_rule_data_list[10],
    "Ultimate Craving CoP Quest (3)": location_rule_data_list[10],
    "Ultimate Craving CoP Quest (4)": location_rule_data_list[10],
    "Spell for Spell CoP Quest (1)": location_rule_data_list[10],
    "Spell for Spell CoP Quest (2)": location_rule_data_list[10],
    "Spell for Spell CoP Quest (3)": location_rule_data_list[10],
    "Unfired Firework CoP Quest (1)": location_rule_data_list[80],
    "Unfired Firework CoP Quest (2)": location_rule_data_list[80],
    "Unfired Firework CoP Quest (3)": location_rule_data_list[80],
    "Time Doesn't Heal CoP Quest (1)": location_rule_data_list[81],
    "Time Doesn't Heal CoP Quest (2)": location_rule_data_list[81],
    "Time Doesn't Heal CoP Quest (3)": location_rule_data_list[81],
    "A Man for a Chocobo Girl CoP Quest (1)": location_rule_data_list[82],
    "A Man for a Chocobo Girl CoP Quest (2)": location_rule_data_list[82],
    "A Man for a Chocobo Girl CoP Quest (3)": location_rule_data_list[82],
    "Rebuilding CoP Quest (1)": location_rule_data_list[80],
    "Rebuilding CoP Quest (2)": location_rule_data_list[80],
    "Global: Key To Her Heart CoP Quest (1)": location_rule_data_list[83],
    "Global: Key To Her Heart CoP Quest (2)": location_rule_data_list[83],
    "Global: Key To Her Heart CoP Quest (3)": location_rule_data_list[83],
    "Global: Roadworks I CoP Quest (1)": location_rule_data_list[70],
    "Global: Roadworks I CoP Quest (2)": location_rule_data_list[70],
    "Global: Roadworks I CoP Quest (3)": location_rule_data_list[70],
    "Global: Roadworks II CoP Quest (1)": location_rule_data_list[84],
    "Global: Roadworks II CoP Quest (2)": location_rule_data_list[84],
    "Global: Roadworks II CoP Quest (3)": location_rule_data_list[84],
    "Global: Roadworks III CoP Quest (1)": location_rule_data_list[85],
    "Global: Roadworks III CoP Quest (2)": location_rule_data_list[85],
    "Global: Roadworks III CoP Quest (3)": location_rule_data_list[85],
    "Global: A Girl's Challenge CoP Quest (1)": location_rule_data_list[86],
    "Global: A Girl's Challenge CoP Quest (2)": location_rule_data_list[86],
    "Global: What's Left Behind CoP Quest (1)": location_rule_data_list[87],
    "Global: What's Left Behind CoP Quest (2)": location_rule_data_list[87],
    "Global: Seeing The Dawn CoP Quest (1)": location_rule_data_list[88],
    "Global: Seeing The Dawn CoP Quest (2)": location_rule_data_list[88],
    "Global: Staying Sharp CoP Quest (1)": location_rule_data_list[89],
    "Global: Staying Sharp CoP Quest (2)": location_rule_data_list[89],
    "Global: Where Moogles Be CoP Quest (1)": location_rule_data_list[90],
    "Global: Where Moogles Be CoP Quest (2)": location_rule_data_list[90],
    "Global: Fading Prayer CoP Quest (1)": location_rule_data_list[91],
    "Global: Fading Prayer CoP Quest (2)": location_rule_data_list[91],
    "Global: Forbidden Tome CoP Quest (1)": location_rule_data_list[92],
    "Global: Forbidden Tome CoP Quest (2)": location_rule_data_list[92],
    "Global: Shoot For The Sky CoP Quest (1)": location_rule_data_list[93],
    "Global: Shoot For The Sky CoP Quest (2)": location_rule_data_list[93],
    "Global: Shoot For The Sky CoP Quest (3)": location_rule_data_list[93],
    "Global: Digging Mysteries CoP Quest (1)": location_rule_data_list[94],
    "Global: Digging Mysteries CoP Quest (2)": location_rule_data_list[94],
    "Global: Digging Mysteries CoP Quest (3)": location_rule_data_list[94],
    "10 Soul Seeds": location_rule_data_list[95],
    "20 Soul Seeds": location_rule_data_list[95],
    "30 Soul Seeds": location_rule_data_list[95],
    "40 Soul Seeds": location_rule_data_list[95],
    "50 Soul Seeds": location_rule_data_list[95],
    "Soul Seeds Fragment of Radiance": location_rule_data_list[96],
    "1 Unappraised": location_rule_data_list[97],
    "5 Unappraised": location_rule_data_list[97],
    "10 Unappraised": location_rule_data_list[97],
    "20 Unappraised": location_rule_data_list[97],
    "50 Unappraised": location_rule_data_list[97],
    "Hoplite Omega Drop (1F)": location_rule_data_list[0],
    "Niblet Omega Drop (2F)": location_rule_data_list[0],
    "Zaltys Omega Drop (3F)": location_rule_data_list[0],
    "Gaunt Omega Drop (4F)": location_rule_data_list[0],
    "Gremlin Omega Drop (5F)": location_rule_data_list[0],
    "Dreadnought Omega Drop (6F)": location_rule_data_list[0],
    "Gorgonopsid Omega Drop (7F)": location_rule_data_list[0],
    "Goblot Omega Drop (8F)": location_rule_data_list[0],
    "Gurangatch Omega Drop (9F)": location_rule_data_list[0],
    "Ectopudding Omega Drop (10F)": location_rule_data_list[0],
    "Miniflan Omega Drop (11F)": location_rule_data_list[0],
    "Aster Protoflorian Omega Drop (12F)": location_rule_data_list[0],
    "Schrodinger Omega Drop (13F)": location_rule_data_list[0],
    "Goblin Omega Drop (14F)": location_rule_data_list[0],
    "Reaver Omega Drop (15F)": location_rule_data_list[0],
    "Meonekton Omega Drop (16F)": location_rule_data_list[0],
    "Cactuar Omega Drop (17F)": location_rule_data_list[0],
    "Triffid Omega Drop (18F)": location_rule_data_list[0],
    "Cyclops Omega Drop (19F)": location_rule_data_list[0],
    "Skeleton Omega Drop (20F)": location_rule_data_list[0],
    "Desert Sahagin Omega Drop (21F)": location_rule_data_list[0],
    "Earth Eater Omega Drop (22F)": location_rule_data_list[0],
    "Skata'ne Omega Drop (23F)": location_rule_data_list[0],
    "Hanuman Omega Drop (24F)": location_rule_data_list[0],
    "Zomok Omega Drop (25F)": location_rule_data_list[0],
    "Dryad Omega Drop (26F)": location_rule_data_list[0],
    "Rafflesia Omega Drop (27F)": location_rule_data_list[0],
    "Chocobo Eater Omega Drop (28F)": location_rule_data_list[0],
    "Ultimate Lair Floor 29": location_rule_data_list[0],
    "Ultimate Lair Floor 30": location_rule_data_list[0],
    "Ultimate Lair Floor 31": location_rule_data_list[0],
    "Ultimate Lair Floor 32": location_rule_data_list[0],
    "Ultimate Lair Boss Drop": location_rule_data_list[71],
    "Ultimate Lair Boss Reward": location_rule_data_list[71],
    "Arcangeli Omega Drop": location_rule_data_list[73],
    "Sugriva Omega Drop": location_rule_data_list[73],
    "Chimera Omega Drop": location_rule_data_list[73],
    "Final Day Altar Of Salvation": location_rule_data_list[73],
    "Final Day Altar Of Judgment": location_rule_data_list[73],
    "Final Day Altar Of Atonement": location_rule_data_list[73],
    "Final Day Altar Of Birth": location_rule_data_list[73],
    "Final Day Temple Of Light (1)": location_rule_data_list[73],
    "Final Day Temple Of Light (2)": location_rule_data_list[73],
    "Final Day Temple Of Light (3)": location_rule_data_list[73],
    "Final Day Ultima Weapon": location_rule_data_list[73],
    "Final Day Ultima Shield": location_rule_data_list[73],
    "Cactair Fragment of Kindness": location_rule_data_list[0],
    "Goblots Arithmometer": location_rule_data_list[0],
    "Aeronite Monster Flesh": location_rule_data_list[71],
    "Zomok Cursed Dragon Claw": location_rule_data_list[0],
    "Gremlins Music Satchel": location_rule_data_list[0],
    "Schrodinger Civet Musk": location_rule_data_list[0],
    "Ark Day 0 Event (1)": location_rule_data_list[0],
    "Ark Day 1 Event (1)": location_rule_data_list[1],
    "Ark Day 2 Event (1)": location_rule_data_list[12],
    "Ark Day 3 Event (1)": location_rule_data_list[14],
    "Ark Day 4 Event (1)": location_rule_data_list[66],
    "Ark Day 5 Event (1)": location_rule_data_list[31],
    "Ark Day 6 Event (1)": location_rule_data_list[67],
    "Main Quest 4 Event (1)": location_rule_data_list[11],
    "Main Quest 4 Event (2)": location_rule_data_list[11],
    "Main Quest 1 Event (1)": location_rule_data_list[12],
    "Main Quest 1 Event (2)": location_rule_data_list[12],
    "Main Quest 3 Event (1)": location_rule_data_list[33],
    "Main Quest 3 Event (2)": location_rule_data_list[33],
    "Main Quest 2 Event (1)": location_rule_data_list[65],
    "Main Quest 2 Event (2)": location_rule_data_list[65],
    "Main Quest 5 Event (1)": location_rule_data_list[41],
    "The Things She Lost Quest Event (1)": location_rule_data_list[16],
    "Where Are You, Holmes? Quest Event (1)": location_rule_data_list[1],
    "Like Clockwork Quest Event (1)": location_rule_data_list[12],
    "Dying Wish Quest Event (1)": location_rule_data_list[98],
    "Suspicious Spheres Quest Event (1)": location_rule_data_list[13],
    "Born From Chaos Quest Event (1)": location_rule_data_list[99],
    "Soul Seeds Quest Event (1)": location_rule_data_list[12],
    "Faster Than Lightning Quest Event (1)": location_rule_data_list[12],
    "Treasured Ball Quest Event (1)": location_rule_data_list[23],
    "The Angel's Tears Quest Event (1)": location_rule_data_list[67],
    "The Saint's Stone Quest Event (1)": location_rule_data_list[12],
    "Whither Faith Quest Event (1)": location_rule_data_list[1],
    "The Avid Reader Quest Event (1)": location_rule_data_list[66],
    "Buried Passion Quest Event (1)": location_rule_data_list[100],
    "The Girl Who Cried Wolf Quest Event (1)": location_rule_data_list[14],
    "Stuck in a Gem Quest Event (1)": location_rule_data_list[12],
    "Get the Girl Quest Event (1)": location_rule_data_list[12],
    "A Rose By Any Other Name Quest Event (1)": location_rule_data_list[101],
    "Voices from the Grave Quest Event (1)": location_rule_data_list[14],
    "To Save the Sinless Quest Event (1)": location_rule_data_list[31],
    "The Life of a Machine Quest Event (1)": location_rule_data_list[1],
    "Old Rivals Quest Event (1)": location_rule_data_list[5],
    "His Wife's Dream Quest Event (1)": location_rule_data_list[5],
    "Tool of the Trade Quest Event (1)": location_rule_data_list[6],
    "Adonis's Audition Quest Event (1)": location_rule_data_list[1],
    "What Rough Beast Slouches Quest Event (1)": location_rule_data_list[102],
    "Skeletons In The Closet Quest Event (1)": location_rule_data_list[103],
    "Last One Standing Quest Event (1)": location_rule_data_list[10],
    "A Father's Request Quest Event (1)": location_rule_data_list[45],
    "The Hunter's Challenge Quest Event (1)": location_rule_data_list[33],
    "A Final Cure Quest Event (1)": location_rule_data_list[45],
    "Fuzzy Search Quest Event (1)": location_rule_data_list[12],
    "Round 'em Up Quest Event (1)": location_rule_data_list[45],
    "Chocobo Cheer Quest Event (1)": location_rule_data_list[45],
    "Peace and Quiet, Kupo Quest Event (1)": location_rule_data_list[1],
    "Saving an Angel Quest Event (1)": location_rule_data_list[104],
    "Omega Point Quest Event (1)": location_rule_data_list[105],
    "The Old Man and the Field Quest Event (1)": location_rule_data_list[33],
    "Land of our Forebears Quest Event (1)": location_rule_data_list[78],
    "A Taste of the Past Quest Event (1)": location_rule_data_list[106],
    "Dog, Doctor and Assistant Quest Event (1)": location_rule_data_list[45],
    "The Right Stuff Quest Event (1)": location_rule_data_list[45],
    "The Secret Lives of Sheep Quest Event (1)": location_rule_data_list[33],
    "Where Are You, Moogle? Quest Event (1)": location_rule_data_list[1],
    "Mercy of a Goddess Quest Event (1)": location_rule_data_list[33],
    "The Grail of Valhalla Quest Event (1)": location_rule_data_list[107],
    "To Live in Chaos Quest Event (1)": location_rule_data_list[78],
    "Killing Time Quest Event (1)": location_rule_data_list[104],
    "Matchmaker Quest Event (1)": location_rule_data_list[45],
    "Mother and Daughter Quest Event (1)": location_rule_data_list[45],
    "Fireworks in a Bottle Quest Event (1)": location_rule_data_list[52],
    "The Fighting Actress Quest Event (1)": location_rule_data_list[52],
    "Songless Diva Quest Event (1)": location_rule_data_list[57],
    "Stolen Things Quest Event (1)": location_rule_data_list[58],
    "Fireworks for a Steal Quest Event (1)": location_rule_data_list[52],
    "A Testing Proposition Quest Event (1)": location_rule_data_list[31],
    "Last Date Quest Event (1)": location_rule_data_list[49],
    "Free Will Quest Event (1)": location_rule_data_list[14],
    "Friends Forever Quest Event (1)": location_rule_data_list[49],
    "Family Food Quest Event (1)": location_rule_data_list[59],
    "Tanbam's Taboo Quest Event (1)": location_rule_data_list[49],
    "Play It for Me Quest Event (1)": location_rule_data_list[60],
    "Adoring Adornments Quest Event (1)": location_rule_data_list[108],
    "Adoring Candice Quest Event (1)": location_rule_data_list[49],
    "Death Safari Quest Event (1)": location_rule_data_list[108],
    "Death Game Quest Event (1)": location_rule_data_list[108],
    "Main Quest 1-1 Event (1)": location_rule_data_list[0],
    "Main Quest 1-2 Event (1)": location_rule_data_list[0],
    "Main Quest 1-3 Event (1)": location_rule_data_list[0],
    "Main Quest 1-4 Event (1)": location_rule_data_list[0],
    "Main Quest 2-1 cyclops Event (1)": location_rule_data_list[109],
    "Main Quest 2-1 Event (1)": location_rule_data_list[110],
    "Main Quest 2-2 Event (1)": location_rule_data_list[111],
    "Main Quest 3-1 Event (1)": location_rule_data_list[0],
    "Main Quest 3-2 Event (1)": location_rule_data_list[32],
    "Main Quest 3-3 Flight Event (1)": location_rule_data_list[112],
    "Main Quest 4-1 Event (1)": location_rule_data_list[0],
    "Main Quest 4-2 Event (1)": location_rule_data_list[0],
    "Main Quest 4-3 Event (1)": location_rule_data_list[0],
    "Main Quest 4-4 First Table placed Event (1)": location_rule_data_list[113],
    "Main Quest 4-4 Event (1)": location_rule_data_list[2],
    "Main Quest 5 start Event (1)": location_rule_data_list[114],
    "0-1 Hint Event (1)": location_rule_data_list[0],
    "1-1 Hint Event (1)": location_rule_data_list[1],
    "1-2 Hint Event (1)": location_rule_data_list[12],
    "1-3 Hint Event (1)": location_rule_data_list[12],
    "1-4 Hint Event (1)": location_rule_data_list[12],
    "1-5 Hint Event (1)": location_rule_data_list[12],
    "2-1 Hint Event (1)": location_rule_data_list[52],
    "2-2 Hint Event (1)": location_rule_data_list[115],
    "2-3 Hint Event (1)": location_rule_data_list[65],
    "3-1 Hint Event (1)": location_rule_data_list[1],
    "3-2 Hint Event (1)": location_rule_data_list[45],
    "3-3 Hint Event (1)": location_rule_data_list[33],
    "4-1 Hint Event (1)": location_rule_data_list[1],
    "4-2 Hint Event (1)": location_rule_data_list[1],
    "4-3 Hint Event (1)": location_rule_data_list[1],
    "4-4 Hint Event (1)": location_rule_data_list[116],
    "4-5 Hint Event (1)": location_rule_data_list[11],
    "5-1 Hint Event (1)": location_rule_data_list[41],
    "5-2 Hint Event (1)": location_rule_data_list[104],
    "5-3 Hint Event (1)": location_rule_data_list[117],
    "5-4 Hint Event (1)": location_rule_data_list[118],
    "5-5 Hint Event (1)": location_rule_data_list[104],
    "5-6 Hint Event (1)": location_rule_data_list[1],
}

entrance_rule_data_table: Dict[str, Callable[[CollectionState, int], bool]] = {
    'entrance_rule_0': lambda state, player: (True),
    'entrance_rule_1': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_2': lambda state, player: (True),
    'entrance_rule_3': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_4': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_5': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_6': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_7': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_8': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_9': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_10': lambda state, player: (state.has("Eradia", player, 100)),
    'entrance_rule_11': lambda state, player: (state.has("Eradia", player, 200)),
    'entrance_rule_12': lambda state, player: (state.has("Eradia", player, 1200)),
}
