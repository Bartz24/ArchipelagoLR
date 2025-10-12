from typing import Callable, Dict, List, Tuple
from BaseClasses import CollectionState, Item
from .RuleLogic import state_has_at_least, item_is_category, state_has_category

rule_data_list: List[Callable[[CollectionState, int], bool]] = [
    lambda state, player:
    True,  # Rule 0
    lambda state, player:
    state.has("Tablet", player, 3),  # Rule 1
    lambda state, player:
    state.has("Tablet", player, 2),  # Rule 2
    lambda state, player:
    state.has("MQ4", player, 3),  # Rule 3
    lambda state, player:
    state.has("Arithmometer", player),  # Rule 4
    lambda state, player:
    state.has("Loupe", player),  # Rule 5
    lambda state, player:
    state.has("MQ4", player),  # Rule 6
    lambda state, player:
    (state.has("Monster Flesh", player) and
     state.has("MQ4", player, 3)),  # Rule 7
    lambda state, player:
    (state.has("Tablet", player) and
     state.has("MQ4", player, 4)),  # Rule 8
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("Crux Base", player) and
     state.has("Crux Tip", player) and
     state.has("Crux Body", player)),  # Rule 9
    lambda state, player:
    state.has("Supply Sphere Password", player),  # Rule 10
    lambda state, player:
    state.has("MQ1", player, 3),  # Rule 11
    lambda state, player:
    state.has("MQ1", player, 4),  # Rule 12
    lambda state, player:
    state.has("MQ1", player, 5),  # Rule 13
    lambda state, player:
    state.has("Day", player, 2),  # Rule 14
    lambda state, player:
    state.has("MQ1", player, 2),  # Rule 15
    lambda state, player:
    (state.has("Thunderclap Cap", player) and
     state.has("Shaolong Gui Shell", player) and
     state.has("Mandragora Root", player)),  # Rule 16
    lambda state, player:
    (state.has("Green Carbuncle Doll", player) and
     state.has("Red Carbuncle Doll", player)),  # Rule 17
    lambda state, player:
    (state.has("Spectral Elixir", player) and
     state.has("MQ1", player, 2)),  # Rule 18
    lambda state, player:
    (state.has("Supply Sphere Password", player) and
     state.has("MQ1", player, 2)),  # Rule 19
    lambda state, player:
    (state.has("Cursed Dragon Claw", player) and
     state.has("MQ1", player, 2)),  # Rule 20
    lambda state, player:
    (state.has("Rubber Ball", player) and
     state.has("MQ1", player, 5)),  # Rule 21
    lambda state, player:
    state.has("Rubber Ball", player),  # Rule 22
    lambda state, player:
    state.has("Q_Saint", player),  # Rule 23
    lambda state, player:
    (state.has("Quill Pen", player) and
     True and
     state.has("MQ1", player, 4)),  # Rule 24
    lambda state, player:
    (state.has("Phantom Rose", player) and
     state.has("MQ1", player, 5)),  # Rule 25
    lambda state, player:
    (state.has("Q_BuriedPassion", player) and
     state.has("MQ1", player, 5)),  # Rule 26
    lambda state, player:
    state.has("MQ3", player, 3),  # Rule 27
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("MQ3", player)),  # Rule 28
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Q_RightStuff", player) and
     state.has("MQ3", player)),  # Rule 29
    lambda state, player:
    state.has("Q_RoundUp", player),  # Rule 30
    lambda state, player:
    state.has("MQ3", player, 2),  # Rule 31
    lambda state, player:
    (state.has("Data Recorder", player) and
     state.has("MQ3", player, 3)),  # Rule 32
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Q_Father", player) and
     state.has("MQ3", player)),  # Rule 33
    lambda state, player:
    state.has("Q_OldMan", player),  # Rule 34
    lambda state, player:
    (state.has("Aryas Apple", player, 2) and
     state.has("MQ3", player, 2)),  # Rule 35
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Fragment of Mischief", player) and
     state.has("Fragment of Radiance", player) and
     state.has("Fragment of Smiles", player) and
     state.has("Fragment of Courage", player) and
     state.has("Fragment of Kindness", player)),  # Rule 36
    lambda state, player:
    state.has("Q_Peace", player),  # Rule 37
    lambda state, player:
    state.has("Q_Cure", player),  # Rule 38
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Goddess Glyphs", player) and
     state.has("Chaos Glyphs", player) and
     state.has("Plate Metal Fragment", player) and
     state.has("Silvered Metal Fragment", player) and
     state.has("Golden Metal Fragment", player) and
     state.has("MQ3", player, 3)),  # Rule 39
    lambda state, player:
    state.has("MQ3", player, 4),  # Rule 40
    lambda state, player:
    (state.has("Q_DDA", player) and
     state.has("Q_RoundUp", player)),  # Rule 41
    lambda state, player:
    state.has("Q_DDA", player),  # Rule 42
    lambda state, player:
    (state.has("Goddess Glyphs", player) and
     state.has("Chaos Glyphs", player) and
     state.has("MQ3", player, 3)),  # Rule 43
    lambda state, player:
    state.has("MQ2", player, 2),  # Rule 44
    lambda state, player:
    state.has("MQ2", player),  # Rule 45
    lambda state, player:
    state.has("Musical Treasure Sphere Key", player),  # Rule 46
    lambda state, player:
    state.has("MQ2", player, 3),  # Rule 47
    lambda state, player:
    state.has("MQ5", player),  # Rule 48
    lambda state, player:
    state.has("MQ2", player, 4),  # Rule 49
    lambda state, player:
    (state.has("MQ2", player, 2) and
     state.has("Midnight Mauve", player)),  # Rule 50
    lambda state, player:
    state.has("Music Satchel", player),  # Rule 51
    lambda state, player:
    state.has("Father's Letter", player),  # Rule 52
    lambda state, player:
    (state.has("Civet Musk", player) and
     state.has("Gordon Gourmet's Recipe", player) and
     state.has("Steak a la Civet", player)),  # Rule 53
    lambda state, player:
    (state.has("Nostalgic Score: Chorus", player) and
     state.has("Nostalgic Score: Refrain", player) and
     state.has("Nostalgic Score: Coda", player)),  # Rule 54
    lambda state, player:
    (state.has("MQ2", player, 2) and
     state_has_category(state, player, "Adornment", 55)),  # Rule 55
    lambda state, player:
    (state.has("MQ2", player, 4) and
     state.has("Q_Adorn", player)),  # Rule 56
    lambda state, player:
    (state.has("MQ2", player, 2) and
     state.has("Q_Death", player)),  # Rule 57
    lambda state, player:
    state.has("Civet Musk", player),  # Rule 58
    lambda state, player:
    (state.has("Civet Musk", player) and
     state.has("Gordon Gourmet's Recipe", player)),  # Rule 59
    lambda state, player:
    state.has("Day", player),  # Rule 60
    lambda state, player:
    state.has("Day", player, 3),  # Rule 61
    lambda state, player:
    state.has("Day", player, 4),  # Rule 62
    lambda state, player:
    state.has("Day", player, 5),  # Rule 63
    lambda state, player:
    state.has("Day", player, 6),  # Rule 64
    lambda state, player:
    (state.has("MQDone", player) and
     state.has("Day", player, 6)),  # Rule 65
    lambda state, player:
    (state.has("MQDone", player, 2) and
     state.has("Day", player, 6)),  # Rule 66
    lambda state, player:
    (state.has("MQDone", player, 3) and
     state.has("Day", player, 6)),  # Rule 67
    lambda state, player:
    (state.has("MQDone", player, 4) and
     state.has("Day", player, 6)),  # Rule 68
    lambda state, player:
    (state.has("MQDone", player, 5) and
     state.has("Day", player, 6)),  # Rule 69
    lambda state, player:
    (state.has("MQDone", player, 5) and
     state.has("Day", player, 6) and
     state.has("MQ1", player, 5) and
     state.has("MQ2", player, 4) and
     state.has("MQ3", player, 4) and
     state.has("MQ4", player, 6) and
     state.has("MQ5", player, 2)),  # Rule 70
    lambda state, player:
    (state.has("C_Miracle", player) and
     state.has("C_Banned", player)),  # Rule 71
    lambda state, player:
    (state.has("C_Child", player) and
     state.has("C_Security", player)),  # Rule 72
    lambda state, player:
    state.has("C_Ranks", player),  # Rule 73
    lambda state, player:
    (state.has("C_Flower", player) and
     state.has("C_Bio", player)),  # Rule 74
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("MQ4", player, 6)),  # Rule 75
    lambda state, player:
    state.has("C_Charm", player),  # Rule 76
    lambda state, player:
    state.has("Q_Food", player),  # Rule 77
    lambda state, player:
    (state.has("Day", player, 6) and
     state.has("MQDone", player) and
     state.has("C_Pride", player)),  # Rule 78
    lambda state, player:
    (state.has("Day", player, 6) and
     state.has("MQDone", player, 3) and
     state.has("C_Pride", player, 2)),  # Rule 79
    lambda state, player:
    state.has("MQ1", player),  # Rule 80
    lambda state, player:
    (state.has("C_Song", player) and
     state.has("C_Grave", player)),  # Rule 81
    lambda state, player:
    (state.has("C_Inventive", player) and
     state.has("C_Puppet", player)),  # Rule 82
    lambda state, player:
    (state.has("C_Slay", player) and
     state.has("C_Teeth", player)),  # Rule 83
    lambda state, player:
    (state.has("C_Revenge", player) and
     state.has("C_Gratitude", player)),  # Rule 84
    lambda state, player:
    (state.has("Proof of Legendary Title", player) and
     state.has("Day", player, 3)),  # Rule 85
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Day", player, 3)),  # Rule 86
    lambda state, player:
    state.has("Q_Hunter", player),  # Rule 87
    lambda state, player:
    state.has("Q_Forebears", player),  # Rule 88
    lambda state, player:
    (state.has("C_Drum", player) and
     state.has("C_Below", player)),  # Rule 89
    lambda state, player:
    (state.has("Day", player, 6) and
     state.has("MQDone", player)),  # Rule 90
    lambda state, player:
    (state.has("C_Forget", player) and
     state.has("C_Thanks", player)),  # Rule 91
    lambda state, player:
    (state.has("C_Fresh", player) and
     state.has("C_Plea", player) and
     state.has("C_Gatekeeper", player)),  # Rule 92
    lambda state, player:
    (state.has("C_Future", player) and
     state.has("C_Brain", player)),  # Rule 93
    lambda state, player:
    state.has("Gysahl Greens", player),  # Rule 94
    lambda state, player:
    state.has("C_Chow", player),  # Rule 95
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Day", player)),  # Rule 96
    lambda state, player:
    (state.has("C_Sun", player) and
     state.has("C_Moon", player)),  # Rule 97
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Q_Peace", player)),  # Rule 98
    lambda state, player:
    (state.has("C_Soulful", player) and
     state.has("C_Inspiration", player)),  # Rule 99
    lambda state, player:
    (state.has("C_Youth", player) and
     state.has("C_Colors", player)),  # Rule 100
    lambda state, player:
    (state.has("C_Secret", player) and
     state.has("C_Dangerous", player) and
     state.has("C_Spell", player)),  # Rule 101
    lambda state, player:
    (state.has("Jade Hair Comb", player) and
     state.has("Bronze Pocket Watch", player) and
     state.has("MQ2", player)),  # Rule 102
    lambda state, player:
    (state.has("Chocobo Girl's Phone No.", player) and
     state.has("Q_Actress", player)),  # Rule 103
    lambda state, player:
    (state.has("Beloved's Gift", player) and
     state.has("MQ5", player)),  # Rule 104
    lambda state, player:
    state.has("MQDone", player, 4),  # Rule 105
    lambda state, player:
    (state.has("Key to the Sand Gate", player) and
     state.has("Key to the Green Gate", player) and
     state.has("MQDone", player, 4)),  # Rule 106
    lambda state, player:
    (state.has("Bandit's Bloodseal", player) and
     state.has("Oath of the Merchants Guild", player) and
     state.has("MQDone", player, 4)),  # Rule 107
    lambda state, player:
    (state.has("Proof of Courage", player) and
     state.has("MQ1", player, 5)),  # Rule 108
    lambda state, player:
    (state.has("Violet Amulet", player) and
     state.has("MQ1", player, 5)),  # Rule 109
    lambda state, player:
    (state.has("Lapis Lazuli", player) and
     state.has("MQ2", player, 4) and
     state.has("C_Girl", player)),  # Rule 110
    lambda state, player:
    (state.has("Power Booster", player) and
     state.has("Q_Death", player)),  # Rule 111
    lambda state, player:
    (state.has("Moogle Dust", player) and
     state.has("MQ3", player, 2)),  # Rule 112
    lambda state, player:
    (state.has("Old-Fashioned Photo Frame", player) and
     state.has("MQ3", player, 2)),  # Rule 113
    lambda state, player:
    (state.has("Etro's Forbidden Tome", player) and
     state.has("MQ3", player, 4)),  # Rule 114
    lambda state, player:
    (state.has("Broken Gyroscope", player) and
     state.has("Day", player, 2)),  # Rule 115
    lambda state, player:
    (state.has("Golden Scarab", player) and
     state.has("MQ4", player, 3)),  # Rule 116
    lambda state, player:
    state.has("Seedhunter Membership Card", player),  # Rule 117
    lambda state, player:
    (state.has("Seedhunter Membership Card", player) and
     state.has("Moogle Fragment", player)),  # Rule 118
    lambda state, player:
    (state.has("MQ4", player, 5) and
     state.has("Crux Base", player) and
     state.has("Crux Tip", player) and
     state.has("Crux Body", player)),  # Rule 119
    lambda state, player:
    (state.has("MQ1", player, 4) and
     state.has("Day", player, 2)),  # Rule 120
    lambda state, player:
    (state.has("MQ3", player, 3) and
     state.has("Day", player, 3)),  # Rule 121
    lambda state, player:
    (state.has("MQ2", player, 3) and
     state.has("Serah's Pendant", player) and
     state.has("Day", player, 3)),  # Rule 122
    lambda state, player:
    (state.has("MQ3", player, 3) and
     state.has("Fragment of Mischief", player) and
     state.has("Fragment of Radiance", player) and
     state.has("Fragment of Smiles", player) and
     state.has("Fragment of Courage", player) and
     state.has("Fragment of Kindness", player) and
     state.has("Day", player, 3)),  # Rule 123
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     True),  # Rule 124
    lambda state, player:
    (state.has("MQ2", player) and
     state.has("ID Card", player)),  # Rule 125
    lambda state, player:
    (state.has("MQ3", player) and
     state.has("Gysahl Greens", player)),  # Rule 126
    lambda state, player:
    state.has("MQ4", player, 2),  # Rule 127
    lambda state, player:
    (state.has("MQ4", player, 3) and
     state.has("Tablet", player)),  # Rule 128
    lambda state, player:
    (state.has("MQ4", player, 4) and
     state.has("Tablet", player, 3)),  # Rule 129
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("MQ3", player, 3)),  # Rule 130
    lambda state, player:
    state.has("MQDone", player, 5),  # Rule 131
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("MQ2", player, 2)),  # Rule 132
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("MQ2", player, 3)),  # Rule 133
    lambda state, player:
    (state.has("Sneaking-In Special Ticket", player) and
     state.has("ID Card", player) and
     state.has("Midnight Mauve", player) and
     state.has("Serah's Pendant", player) and
     state.has("MQ2", player, 4)),  # Rule 134
    lambda state, player:
    state.has("MQ3", player),  # Rule 135
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("MQ3", player, 2)),  # Rule 136
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("MQ3", player, 4)),  # Rule 137
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("MQ4", player, 5)),  # Rule 138
    lambda state, player:
    (state.has("Tablet", player, 3) and
     state.has("Crux Base", player) and
     state.has("Crux Tip", player) and
     state.has("Crux Body", player) and
     state.has("MQ4", player, 6)),  # Rule 139
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("Fragment of Mischief", player) and
     state.has("Fragment of Radiance", player) and
     state.has("Fragment of Smiles", player) and
     state.has("Fragment of Courage", player) and
     state.has("Fragment of Kindness", player) and
     state.has("MQ5", player)),  # Rule 140
    lambda state, player:
    (state.has("Gysahl Greens", player) and
     state.has("MQ5", player)),  # Rule 141
    lambda state, player:
    (state.has("Beloved's Gift", player) and
     state.has("Gysahl Greens", player) and
     state.has("MQ5", player)),  # Rule 142
    lambda state, player:
    (state.has("Moogle Fragment", player) and
     state.has("Gysahl Greens", player) and
     state.has("Seedhunter Membership Card", player) and
     state.has("MQ5", player)),  # Rule 143
]

location_rule_data_table: Dict[str, Callable[[CollectionState, int], bool]] = {
    "Dead Dunes - Golden Scarab Treasure": rule_data_list[0],
    "Dead Dunes - Oasis Lighthouse Treasure (1)": rule_data_list[0],
    "Dead Dunes - Grave of the Colossi Shrine Treasure": rule_data_list[0],
    "Dead Dunes - Giant's Sandbox Treasure (1)": rule_data_list[0],
    "Dead Dunes - Golden Chamber Lower Treasure": rule_data_list[0],
    "Dead Dunes - Giant's Sandbox Treasure (2)": rule_data_list[0],
    "Dead Dunes - Giant's Sandbox Treasure (3)": rule_data_list[0],
    "Dead Dunes - Giant's Sandbox Treasure (4)": rule_data_list[0],
    "Dead Dunes - Ruffian Outdoor Treasure": rule_data_list[0],
    "Dead Dunes - Dry Floodlands Treasure (1)": rule_data_list[0],
    "Dead Dunes - Oasis Lighthouse Treasure (2)": rule_data_list[0],
    "Dead Dunes - Oasis Lighthouse Treasure (3)": rule_data_list[0],
    "Dead Dunes - Atomos's Sand Treasure (1)": rule_data_list[0],
    "Dead Dunes - Grave of the Colossi Treasure (1)": rule_data_list[0],
    "Dead Dunes - Grave of the Colossi Treasure (2)": rule_data_list[0],
    "Dead Dunes - Grave of the Colossi Treasure (3)": rule_data_list[0],
    "Dead Dunes - Atomos's Sand Treasure (2)": rule_data_list[0],
    "Dead Dunes - Ruffian 2nd Floor Treasure": rule_data_list[0],
    "Dead Dunes - Temple Ruins Chamber of Dusk (Upper) Treasure": rule_data_list[0],
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Upper) Treasure (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Upper) Treasure (2)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Upper) Treasure (3)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Lower) Treasure (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Lower) Treasure (2)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Lower) Treasure (3)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Sacred Grove Treasure": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Treasure (1)": rule_data_list[0],
    "Dead Dunes - Dry Floodlands Shrine Treasure": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Treasure (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Treasure (2)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Treasure (3)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Scorched Earth (Lower) Treasure": rule_data_list[0],
    "Dead Dunes - Temple Ruins Scorched Earth (Upper) Treasure (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Scorched Earth (Upper) Treasure (2)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Treasure (2)": rule_data_list[0],
    "Dead Dunes - Atomos's Sands Shrine Treasure": rule_data_list[0],
    "Dead Dunes - Giant's Sandbox Treasure (5)": rule_data_list[0],
    "Dead Dunes - Dry Floodlands Treasure (2)": rule_data_list[0],
    "Dead Dunes - Grave of the Colossi Shrine Tablet": rule_data_list[0],
    "Dead Dunes - Dry Floodlands Shrine Tablet": rule_data_list[0],
    "Dead Dunes - Atomos's Sands Shrine Tablet": rule_data_list[0],
    "Dead Dunes - Temple Ruins Mural Crux Base": rule_data_list[1],
    "Dead Dunes - Temple Ruins Mural Crux Body": rule_data_list[2],
    "Dead Dunes - Temple Ruins Mural Crux Tip": rule_data_list[2],
    "Dead Dunes - Temple Ruins Bhakti Reward": rule_data_list[0],
    "Dead Dunes - Grave of the Colossi Pilgrim's Crux": rule_data_list[0],
    "Dead Dunes - Temple Ruins Scorched Earth Pilgrim's Crux (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Scorched Earth Pilgrim's Crux (2)": rule_data_list[0],
    "Dead Dunes - Dry Floodlands Pilgrim's Crux": rule_data_list[0],
    "Dead Dunes - Atomos's Sands Pilgrim's Crux": rule_data_list[0],
    "Dead Dunes - Giant's Sandbox Pilgrim's Crux": rule_data_list[0],
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (2)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (1)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (3)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (2)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (4)": rule_data_list[0],
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (2)": rule_data_list[0],
    "Dead Dunes - Atomos's Sands Loupe": rule_data_list[0],
    "Dead Dunes - The Life of a Machine Quest (1)": rule_data_list[3],
    "Dead Dunes - The Life of a Machine Quest (2)": rule_data_list[3],
    "Dead Dunes - Old Rivals Quest (1)": rule_data_list[4],
    "Dead Dunes - Old Rivals Quest (2)": rule_data_list[4],
    "Dead Dunes - His Wife's Dream Quest (1)": rule_data_list[4],
    "Dead Dunes - His Wife's Dream Quest (2)": rule_data_list[4],
    "Dead Dunes - Tool of the Trade Quest (1)": rule_data_list[5],
    "Dead Dunes - Tool of the Trade Quest (2)": rule_data_list[5],
    "Dead Dunes - Adonis's Audition Quest (1)": rule_data_list[6],
    "Dead Dunes - Adonis's Audition Quest (2)": rule_data_list[6],
    "Dead Dunes - What Rough Beast Slouches Quest (1)": rule_data_list[7],
    "Dead Dunes - What Rough Beast Slouches Quest (2)": rule_data_list[7],
    "Dead Dunes - Skeletons In The Closet Quest (1)": rule_data_list[8],
    "Dead Dunes - Skeletons In The Closet Quest (2)": rule_data_list[8],
    "Dead Dunes - Last One Standing Quest (1)": rule_data_list[0],
    "Dead Dunes - Last One Standing Quest (2)": rule_data_list[0],
    "Dead Dunes - Last One Standing Quest (3)": rule_data_list[0],
    "Dead Dunes - What Rough Beast Slouches Libra Notes": rule_data_list[3],
    "Dead Dunes - Dead Dunes Boss Drop": rule_data_list[9],
    "Dead Dunes - Aeronite Missable Drop": rule_data_list[0],
    "Luxerion - Cathedral Proof Of Courage": rule_data_list[0],
    "Luxerion - Pilgrim's Passage Violet Amulet Treasure": rule_data_list[0],
    "Luxerion - North Station Plaza Treasure": rule_data_list[0],
    "Luxerion - The Avenue Treasure": rule_data_list[0],
    "Luxerion - Gallery Steps Treasure": rule_data_list[0],
    "Luxerion - 2nd Ave Treasure": rule_data_list[0],
    "Luxerion - Pilgrim's Passage (Grassy) Treasure": rule_data_list[0],
    "Luxerion - Old Theater Platform Treasure": rule_data_list[0],
    "Luxerion - The Warren Mangled Hill Treasure": rule_data_list[0],
    "Luxerion - South Station (Supply Sphere) Treasure": rule_data_list[10],
    "Luxerion - Warehouse District (Supply Sphere) Treasure": rule_data_list[10],
    "Luxerion - Residences (Supply Sphere) Treasure": rule_data_list[10],
    "Luxerion - Forsaken Graveyard Treasure (1)": rule_data_list[11],
    "Luxerion - Den Of Shadows Treasure (1)": rule_data_list[12],
    "Luxerion - Luxerion After 1st Phone (1)": rule_data_list[0],
    "Luxerion - Den Of Shadows Treasure (2)": rule_data_list[12],
    "Luxerion - Luxerion After 1st Phone (2)": rule_data_list[0],
    "Luxerion - Luxerion After 1st Phone (3)": rule_data_list[0],
    "Luxerion - Luxerion Marketplace Treasure": rule_data_list[0],
    "Luxerion - Forsaken Graveyard Treasure (2)": rule_data_list[11],
    "Luxerion - 1st Ave Rubber Ball": rule_data_list[13],
    "Luxerion - Marketplace Doll": rule_data_list[0],
    "Luxerion - North Station Plaza Doll": rule_data_list[0],
    "Luxerion - Warehouse District Thunderclap Cap": rule_data_list[0],
    "Luxerion - Luxerion Proof of Legendary Title": rule_data_list[14],
    "Luxerion - Luxerion Ghost Phantom Rose": rule_data_list[0],
    "Luxerion - Luxerion Marketplace Pen": rule_data_list[0],
    "Luxerion - Baird Seedhunter Membership Card": rule_data_list[0],
    "Luxerion - Virgil Supply Sphere Password": rule_data_list[15],
    "Luxerion - Buy Shaolong Gui Shell": rule_data_list[0],
    "Luxerion - Buy Mandragora Root": rule_data_list[0],
    "Luxerion - Chocobo Emporium Spectral Elixir": rule_data_list[16],
    "Luxerion - The Things She Lost Quest (1)": rule_data_list[17],
    "Luxerion - The Things She Lost Quest (2)": rule_data_list[17],
    "Luxerion - Where Are You, Holmes? Quest (1)": rule_data_list[0],
    "Luxerion - Where Are You, Holmes? Quest (2)": rule_data_list[0],
    "Luxerion - Where Are You, Holmes? Quest (3)": rule_data_list[0],
    "Luxerion - Like Clockwork Quest (1)": rule_data_list[12],
    "Luxerion - Like Clockwork Quest (2)": rule_data_list[12],
    "Luxerion - Dying Wish Quest (1)": rule_data_list[18],
    "Luxerion - Dying Wish Quest (2)": rule_data_list[18],
    "Luxerion - Suspicious Spheres Quest (1)": rule_data_list[19],
    "Luxerion - Suspicious Spheres Quest (2)": rule_data_list[19],
    "Luxerion - Born From Chaos Quest (1)": rule_data_list[20],
    "Luxerion - Born From Chaos Quest (2)": rule_data_list[20],
    "Luxerion - Born From Chaos Quest (3)": rule_data_list[20],
    "Luxerion - Born From Chaos Quest (4)": rule_data_list[20],
    "Luxerion - Soul Seeds Quest (1)": rule_data_list[15],
    "Luxerion - Soul Seeds Quest (2)": rule_data_list[15],
    "Luxerion - Faster Than Lightning Quest (1)": rule_data_list[15],
    "Luxerion - Faster Than Lightning Quest (2)": rule_data_list[15],
    "Luxerion - Treasured Ball Quest (1)": rule_data_list[21],
    "Luxerion - Treasured Ball Quest (2)": rule_data_list[21],
    "Luxerion - Talbot's Gratitude": rule_data_list[22],
    "Luxerion - The Angel's Tears Quest (1)": rule_data_list[15],
    "Luxerion - The Angel's Tears Quest (2)": rule_data_list[15],
    "Luxerion - The Saint's Stone Quest (1)": rule_data_list[13],
    "Luxerion - The Saint's Stone Quest (2)": rule_data_list[13],
    "Luxerion - The Saint's Stone Quest (3)": rule_data_list[13],
    "Luxerion - Aremiah Service Entrance Key": rule_data_list[23],
    "Luxerion - Whither Faith Quest (1)": rule_data_list[0],
    "Luxerion - Whither Faith Quest (2)": rule_data_list[0],
    "Luxerion - The Avid Reader Quest (1)": rule_data_list[13],
    "Luxerion - The Avid Reader Quest (2)": rule_data_list[13],
    "Luxerion - Buried Passion Quest (1)": rule_data_list[24],
    "Luxerion - Buried Passion Quest (2)": rule_data_list[24],
    "Luxerion - The Girl Who Cried Wolf Quest (1)": rule_data_list[13],
    "Luxerion - The Girl Who Cried Wolf Quest (2)": rule_data_list[13],
    "Luxerion - Stuck in a Gem Quest (1)": rule_data_list[0],
    "Luxerion - Stuck in a Gem Quest (2)": rule_data_list[0],
    "Luxerion - Get the Girl Quest (1)": rule_data_list[13],
    "Luxerion - Get the Girl Quest (2)": rule_data_list[13],
    "Luxerion - A Rose By Any Other Name Quest (1)": rule_data_list[25],
    "Luxerion - A Rose By Any Other Name Quest (2)": rule_data_list[25],
    "Luxerion - A Rose By Any Other Name Quest (3)": rule_data_list[25],
    "Luxerion - A Rose By Any Other Name Quest (4)": rule_data_list[25],
    "Luxerion - Voices from the Grave Quest (1)": rule_data_list[13],
    "Luxerion - Voices from the Grave Quest (2)": rule_data_list[13],
    "Luxerion - To Save the Sinless Quest (1)": rule_data_list[26],
    "Luxerion - To Save the Sinless Quest (2)": rule_data_list[26],
    "Luxerion - Replace Chronostasis": rule_data_list[0],
    "Luxerion - Luxerion Boss Drop": rule_data_list[12],
    "Luxerion - Luxerion Boss+ Only Missable Drop": rule_data_list[12],
    "Wildlands - Moogle Village Moogle Dust Treasure": rule_data_list[0],
    "Wildlands - Research Camp Photo Frame Treasure": rule_data_list[0],
    "Wildlands - Poltae Etro's Forbidden Tome": rule_data_list[0],
    "Wildlands - Eremite Plains Broken Gyroscope Treasure": rule_data_list[27],
    "Wildlands - Aryas Village Treasure (1)": rule_data_list[0],
    "Wildlands - Jagd Woods Treasure": rule_data_list[27],
    "Wildlands - The Grasslands Treasure (1)": rule_data_list[27],
    "Wildlands - Poltae Treasure (1)": rule_data_list[27],
    "Wildlands - Canopus Farms Treasure": rule_data_list[0],
    "Wildlands - Rocky Crag Treasure (1)": rule_data_list[27],
    "Wildlands - The Grasslands Treasure (2)": rule_data_list[27],
    "Wildlands - Aryas Village Treasure (2)": rule_data_list[0],
    "Wildlands - The Grasslands Treasure (3)": rule_data_list[27],
    "Wildlands - Eremite Plains Treasure (1)": rule_data_list[27],
    "Wildlands - Eremite Plains Treasure (2)": rule_data_list[27],
    "Wildlands - Moogle Village Treasure": rule_data_list[27],
    "Wildlands - City of Ruins Treasure": rule_data_list[27],
    "Wildlands - Rocky Crag Treasure (2)": rule_data_list[27],
    "Wildlands - Rocky Crag Treasure (3)": rule_data_list[27],
    "Wildlands - Aryas Village Treasure (3)": rule_data_list[27],
    "Wildlands - Poltae Treasure (2)": rule_data_list[0],
    "Wildlands - Eremite Plains Crash Site Fragment": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (1)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (2)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (3)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (4)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (5)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (6)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (7)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (8)": rule_data_list[27],
    "Wildlands - Goddess Temple Treasure (9)": rule_data_list[27],
    "Wildlands - Dr Gysahl's Gysahl Greens": rule_data_list[0],
    "Wildlands - Aryas Village Beloved's Gift Treasure": rule_data_list[0],
    "Wildlands - Sarala Vegatable Seeds": rule_data_list[28],
    "Wildlands - A Father's Request Quest (1)": rule_data_list[28],
    "Wildlands - A Father's Request Quest (2)": rule_data_list[28],
    "Wildlands - The Hunter's Challenge Quest (1)": rule_data_list[29],
    "Wildlands - The Hunter's Challenge Quest (2)": rule_data_list[29],
    "Wildlands - The Hunter's Challenge Quest (3)": rule_data_list[29],
    "Wildlands - A Final Cure Quest (1)": rule_data_list[28],
    "Wildlands - A Final Cure Quest (2)": rule_data_list[28],
    "Wildlands - A Final Cure Quest (3)": rule_data_list[28],
    "Wildlands - Fuzzy Search Quest (1)": rule_data_list[30],
    "Wildlands - Fuzzy Search Quest (2)": rule_data_list[30],
    "Wildlands - Fuzzy Search Quest (3)": rule_data_list[30],
    "Wildlands - Round 'em Up Quest (1)": rule_data_list[31],
    "Wildlands - Round 'em Up Quest (2)": rule_data_list[31],
    "Wildlands - Chocobo Cheer Quest (1)": rule_data_list[31],
    "Wildlands - Chocobo Cheer Quest (2)": rule_data_list[31],
    "Wildlands - Chocobo Cheer Quest (3)": rule_data_list[31],
    "Wildlands - Peace and Quiet, Kupo Quest (1)": rule_data_list[0],
    "Wildlands - Peace and Quiet, Kupo Quest (2)": rule_data_list[0],
    "Wildlands - Peace and Quiet, Kupo Quest (3)": rule_data_list[0],
    "Wildlands - Saving an Angel Quest (1)": rule_data_list[28],
    "Wildlands - Saving an Angel Quest (2)": rule_data_list[28],
    "Wildlands - Omega Point Quest (1)": rule_data_list[32],
    "Wildlands - Omega Point Quest (2)": rule_data_list[32],
    "Wildlands - The Old Man and the Field Quest (1)": rule_data_list[33],
    "Wildlands - The Old Man and the Field Quest (2)": rule_data_list[33],
    "Wildlands - Land of our Forebears Quest (1)": rule_data_list[34],
    "Wildlands - Land of our Forebears Quest (2)": rule_data_list[34],
    "Wildlands - A Taste of the Past Quest (1)": rule_data_list[35],
    "Wildlands - A Taste of the Past Quest (2)": rule_data_list[35],
    "Wildlands - A Taste of the Past Quest (3)": rule_data_list[35],
    "Wildlands - Dog, Doctor and Assistant Quest (1)": rule_data_list[31],
    "Wildlands - Dog, Doctor and Assistant Quest (2)": rule_data_list[31],
    "Wildlands - Main Quest 5 (1)": rule_data_list[36],
    "Wildlands - Main Quest 5 (2)": rule_data_list[36],
    "Wildlands - Main Quest 5 (3)": rule_data_list[36],
    "Wildlands - The Right Stuff Quest (1)": rule_data_list[28],
    "Wildlands - The Right Stuff Quest (2)": rule_data_list[28],
    "Wildlands - The Secret Lives of Sheep Quest (1)": rule_data_list[30],
    "Wildlands - The Secret Lives of Sheep Quest (2)": rule_data_list[30],
    "Wildlands - Where Are You, Moogle? Quest (1)": rule_data_list[37],
    "Wildlands - Where Are You, Moogle? Quest (2)": rule_data_list[37],
    "Wildlands - Where Are You, Moogle? Quest (3)": rule_data_list[37],
    "Wildlands - Mercy of a Goddess Quest (1)": rule_data_list[38],
    "Wildlands - Mercy of a Goddess Quest (2)": rule_data_list[38],
    "Wildlands - The Grail of Valhalla Quest (1)": rule_data_list[39],
    "Wildlands - The Grail of Valhalla Quest (2)": rule_data_list[39],
    "Wildlands - The Grail of Valhalla Quest (3)": rule_data_list[39],
    "Wildlands - To Live in Chaos Quest (1)": rule_data_list[40],
    "Wildlands - To Live in Chaos Quest (2)": rule_data_list[40],
    "Wildlands - To Live in Chaos Quest (3)": rule_data_list[40],
    "Wildlands - Killing Time Quest (1)": rule_data_list[27],
    "Wildlands - Killing Time Quest (2)": rule_data_list[27],
    "Wildlands - Matchmaker Quest (1)": rule_data_list[41],
    "Wildlands - Matchmaker Quest (2)": rule_data_list[41],
    "Wildlands - Mother and Daughter Quest (1)": rule_data_list[42],
    "Wildlands - Mother and Daughter Quest (2)": rule_data_list[42],
    "Wildlands - The Secret Lives of Sheep Mystery Egg": rule_data_list[30],
    "Wildlands - Goddess Temple Goddess Glyphs": rule_data_list[27],
    "Wildlands - Goddess Temple Chaos Glyphs": rule_data_list[27],
    "Wildlands - Poltae Plate Metal Fragment": rule_data_list[43],
    "Wildlands - Poltae Silvered Metal Fragment": rule_data_list[43],
    "Wildlands - Poltae Gold Metal Fragment": rule_data_list[43],
    "Wildlands - Research Camp Data Recorder": rule_data_list[27],
    "Wildlands - Aryas Village Apple (1)": rule_data_list[27],
    "Wildlands - Aryas Village Apple (2)": rule_data_list[27],
    "Wildlands - Aryas Village Apple (3)": rule_data_list[27],
    "Wildlands - Wildlands Boss Drop": rule_data_list[27],
    "Yusnaan - Reveler's Quarter Lapis Lazuli Treasure": rule_data_list[0],
    "Yusnaan - Industrial Area Power Booster": rule_data_list[44],
    "Yusnaan - Tunnel Oath of the Merchants Guild Treasure": rule_data_list[0],
    "Yusnaan - Industrial Area Jade Hair Comb": rule_data_list[44],
    "Yusnaan - Industrial Area Bronze Pocket Watch": rule_data_list[44],
    "Yusnaan - Chocobo Girl Poster": rule_data_list[0],
    "Yusnaan - Glutton's Quarter Treasure (1)": rule_data_list[0],
    "Yusnaan - Aromatic Market Treasure": rule_data_list[0],
    "Yusnaan - Central Ave Treasure": rule_data_list[0],
    "Yusnaan - Coliseum Square Treasure": rule_data_list[0],
    "Yusnaan - Tour Guide Sneaking-In Special Ticket": rule_data_list[0],
    "Yusnaan - Warehouse District Id Card": rule_data_list[45],
    "Yusnaan - Coliseum Square (Musical) Treasure": rule_data_list[46],
    "Yusnaan - Cactuar Statue (Musical) Treasure": rule_data_list[46],
    "Yusnaan - Station (Musical) Treasure": rule_data_list[46],
    "Yusnaan - Cactuar Statue Treasure": rule_data_list[0],
    "Yusnaan - Reveler's Quarter Treasure (1)": rule_data_list[0],
    "Yusnaan - Augur's Quarter Treasure (1)": rule_data_list[44],
    "Yusnaan - Patron's Palace Treasure (1)": rule_data_list[47],
    "Yusnaan - Hawker's Row Treasure": rule_data_list[0],
    "Yusnaan - Augur's Quarter Treasure (2)": rule_data_list[44],
    "Yusnaan - Warehouse District Treasure": rule_data_list[45],
    "Yusnaan - Augur's Quarter Treasure (3)": rule_data_list[44],
    "Yusnaan - Supply Line Treasure": rule_data_list[45],
    "Yusnaan - Industrial Area Treasure": rule_data_list[45],
    "Yusnaan - Lower City Treasure": rule_data_list[0],
    "Yusnaan - Glutton's Quarter Treasure (2)": rule_data_list[0],
    "Yusnaan - Reveler's Quarter Treasure (2)": rule_data_list[0],
    "Yusnaan - Patron's Palace Treasure (2)": rule_data_list[47],
    "Yusnaan - Patron's Palace Treasure (3)": rule_data_list[47],
    "Yusnaan - Patron's Palace Treasure (4)": rule_data_list[47],
    "Yusnaan - Patron's Palace Treasure (5)": rule_data_list[47],
    "Yusnaan - Slaughterhouse Special Fragment of Courage": rule_data_list[48],
    "Yusnaan - Slaughterhouse (1)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (2)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (3)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (4)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (5)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (6)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (7)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (8)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (9)": rule_data_list[0],
    "Yusnaan - Slaughterhouse (10)": rule_data_list[0],
    "Yusnaan - The Fighting Actress Slaughterhouse (1)": rule_data_list[44],
    "Yusnaan - The Fighting Actress Slaughterhouse (2)": rule_data_list[44],
    "Yusnaan - The Fighting Actress Slaughterhouse (3)": rule_data_list[44],
    "Yusnaan - The Fighting Actress Slaughterhouse (4)": rule_data_list[44],
    "Yusnaan - Tanbam's Taboo Slaughterhouse": rule_data_list[49],
    "Yusnaan - Chocobo Girl Miqo'te Dress": rule_data_list[0],
    "Yusnaan - Director Femme Fetale": rule_data_list[50],
    "Yusnaan - Fireworks in a Bottle Quest (1)": rule_data_list[44],
    "Yusnaan - Fireworks in a Bottle Quest (2)": rule_data_list[44],
    "Yusnaan - The Fighting Actress Quest (1)": rule_data_list[44],
    "Yusnaan - The Fighting Actress Quest (2)": rule_data_list[44],
    "Yusnaan - Songless Diva Quest (1)": rule_data_list[51],
    "Yusnaan - Songless Diva Quest (2)": rule_data_list[51],
    "Yusnaan - Stolen Things Quest (1)": rule_data_list[52],
    "Yusnaan - Stolen Things Quest (2)": rule_data_list[52],
    "Yusnaan - Fireworks for a Steal Quest (1)": rule_data_list[44],
    "Yusnaan - Fireworks for a Steal Quest (2)": rule_data_list[44],
    "Yusnaan - A Testing Proposition Quest (1)": rule_data_list[0],
    "Yusnaan - A Testing Proposition Quest (2)": rule_data_list[0],
    "Yusnaan - Last Date Quest (1)": rule_data_list[49],
    "Yusnaan - Last Date Quest (2)": rule_data_list[49],
    "Yusnaan - Free Will Quest (1)": rule_data_list[0],
    "Yusnaan - Free Will Quest (2)": rule_data_list[0],
    "Yusnaan - Free Will Quest (3)": rule_data_list[0],
    "Yusnaan - Friends Forever Quest (1)": rule_data_list[49],
    "Yusnaan - Friends Forever Quest (2)": rule_data_list[49],
    "Yusnaan - Friends Forever Quest (3)": rule_data_list[49],
    "Yusnaan - Family Food Quest (1)": rule_data_list[53],
    "Yusnaan - Family Food Quest (2)": rule_data_list[53],
    "Yusnaan - Tanbam's Taboo Quest (1)": rule_data_list[49],
    "Yusnaan - Tanbam's Taboo Quest (2)": rule_data_list[49],
    "Yusnaan - Play It for Me Quest (1)": rule_data_list[54],
    "Yusnaan - Play It for Me Quest (2)": rule_data_list[54],
    "Yusnaan - Adoring Adornments Quest (1)": rule_data_list[55],
    "Yusnaan - Adoring Adornments Quest (2)": rule_data_list[55],
    "Yusnaan - Adoring Candice Quest (1)": rule_data_list[56],
    "Yusnaan - Adoring Candice Quest (2)": rule_data_list[56],
    "Yusnaan - Adoring Candice Quest (3)": rule_data_list[56],
    "Yusnaan - Death Safari Quest (1)": rule_data_list[44],
    "Yusnaan - Death Safari Quest (2)": rule_data_list[44],
    "Yusnaan - Death Safari Quest (3)": rule_data_list[44],
    "Yusnaan - Death Safari Quest (4)": rule_data_list[44],
    "Yusnaan - Death Safari Quest (5)": rule_data_list[44],
    "Yusnaan - Death Game Quest (1)": rule_data_list[57],
    "Yusnaan - Death Game Quest (2)": rule_data_list[57],
    "Yusnaan - Death Game Quest (3)": rule_data_list[57],
    "Yusnaan - Morris Musical Treasure Sphere Key": rule_data_list[0],
    "Yusnaan - Patron's Palace Serah's Pendant": rule_data_list[47],
    "Yusnaan - Gordon Gourmet's Recipe": rule_data_list[58],
    "Yusnaan - Seedy Steak a la Civet": rule_data_list[59],
    "Yusnaan - Gregory Father's Letter": rule_data_list[0],
    "Yusnaan - Tanbam's Taboo Libra Notes": rule_data_list[49],
    "Yusnaan - Yusnaan Boss Drop": rule_data_list[47],
    "Ark - Initial 3rd Garb (1)": rule_data_list[0],
    "Ark - Initial 3rd Garb (2)": rule_data_list[0],
    "Ark - Initial 3rd Garb (3)": rule_data_list[0],
    "Ark - Ark Day 1 (1)": rule_data_list[0],
    "Ark - Ark Day 1 (2)": rule_data_list[0],
    "Ark - Ark Day 1 (3)": rule_data_list[0],
    "Ark - Ark Day 1 (4)": rule_data_list[0],
    "Ark - Ark Day 1 (5)": rule_data_list[0],
    "Ark - Ark Day 2 (1)": rule_data_list[60],
    "Ark - Ark Day 2 (2)": rule_data_list[60],
    "Ark - Ark Day 2 (3)": rule_data_list[60],
    "Ark - Ark Day 3 (1)": rule_data_list[14],
    "Ark - Ark Day 4 (1)": rule_data_list[61],
    "Ark - Ark Day 4 (2)": rule_data_list[61],
    "Ark - Ark Day 5 (1)": rule_data_list[62],
    "Ark - Ark Day 6 (1)": rule_data_list[63],
    "Ark - Ark Day 7": rule_data_list[64],
    "Ark - Ark Day 8": rule_data_list[65],
    "Ark - Ark Day 9": rule_data_list[66],
    "Ark - Ark Day 10": rule_data_list[67],
    "Ark - Ark Day 11": rule_data_list[68],
    "Ark - Ark Day 12": rule_data_list[69],
    "Ark - Ark Final Day (1)": rule_data_list[69],
    "Ark - Ark Final Day (2)": rule_data_list[69],
    "Ark - Ark Final Day (3)": rule_data_list[69],
    "Ark - Ark Extra Day": rule_data_list[70],
    "Ark - Replace Curaga": rule_data_list[0],
    "Ark - Replace Teleport": rule_data_list[0],
    "Ark - Replace Escape": rule_data_list[0],
    "CoP Dead Dunes - Flower in the Sands CoP Quest (1)": rule_data_list[60],
    "CoP Dead Dunes - Flower in the Sands CoP Quest (2)": rule_data_list[60],
    "CoP Dead Dunes - Biologically Speaking CoP Quest (1)": rule_data_list[60],
    "CoP Dead Dunes - Biologically Speaking CoP Quest (2)": rule_data_list[60],
    "CoP Dead Dunes - The Real Client CoP Quest (1)": rule_data_list[71],
    "CoP Dead Dunes - The Real Client CoP Quest (2)": rule_data_list[71],
    "CoP Dead Dunes - The Real Client CoP Quest (3)": rule_data_list[71],
    "CoP Dead Dunes - For My Child CoP Quest (1)": rule_data_list[61],
    "CoP Dead Dunes - For My Child CoP Quest (2)": rule_data_list[61],
    "CoP Dead Dunes - For My Child CoP Quest (3)": rule_data_list[61],
    "CoP Dead Dunes - Bandits' New Weapon CoP Quest (1)": rule_data_list[72],
    "CoP Dead Dunes - Bandits' New Weapon CoP Quest (2)": rule_data_list[72],
    "CoP Dead Dunes - Bandits' New Weapon CoP Quest (3)": rule_data_list[72],
    "CoP Dead Dunes - Banned Goods CoP Quest (1)": rule_data_list[60],
    "CoP Dead Dunes - Banned Goods CoP Quest (2)": rule_data_list[60],
    "CoP Dead Dunes - Banned Goods CoP Quest (3)": rule_data_list[60],
    "CoP Dead Dunes - Climbing The Ranks I CoP Quest (1)": rule_data_list[61],
    "CoP Dead Dunes - Climbing The Ranks I CoP Quest (2)": rule_data_list[61],
    "CoP Dead Dunes - Miracle Vintage CoP Quest (1)": rule_data_list[62],
    "CoP Dead Dunes - Miracle Vintage CoP Quest (2)": rule_data_list[62],
    "CoP Dead Dunes - Miracle Vintage CoP Quest (3)": rule_data_list[62],
    "CoP Dead Dunes - Climbing The Ranks II CoP Quest (1)": rule_data_list[73],
    "CoP Dead Dunes - Climbing The Ranks II CoP Quest (2)": rule_data_list[73],
    "CoP Dead Dunes - Heightened Security CoP Quest (1)": rule_data_list[62],
    "CoP Dead Dunes - Heightened Security CoP Quest (2)": rule_data_list[62],
    "CoP Dead Dunes - Heightened Security CoP Quest (3)": rule_data_list[62],
    "CoP Dead Dunes - Desert Cleanup CoP Quest (1)": rule_data_list[74],
    "CoP Dead Dunes - Desert Cleanup CoP Quest (2)": rule_data_list[74],
    "CoP Dead Dunes - Desert Cleanup CoP Quest (3)": rule_data_list[74],
    "CoP Dead Dunes - A Treasure for a God CoP Quest (1)": rule_data_list[75],
    "CoP Dead Dunes - A Treasure for a God CoP Quest (2)": rule_data_list[75],
    "CoP Dead Dunes - Lucky Charm CoP Quest (1)": rule_data_list[0],
    "CoP Dead Dunes - Lucky Charm CoP Quest (2)": rule_data_list[0],
    "CoP Dead Dunes - Supply and Demand CoP Quest (1)": rule_data_list[76],
    "CoP Dead Dunes - Supply and Demand CoP Quest (2)": rule_data_list[76],
    "CoP Dead Dunes - Supply and Demand CoP Quest (3)": rule_data_list[76],
    "CoP Dead Dunes - A New Application CoP Quest (1)": rule_data_list[77],
    "CoP Dead Dunes - A New Application CoP Quest (2)": rule_data_list[77],
    "CoP Dead Dunes - A New Application CoP Quest (3)": rule_data_list[77],
    "CoP Dead Dunes - Pride And Greed I CoP Quest (1)": rule_data_list[61],
    "CoP Dead Dunes - Pride And Greed I CoP Quest (2)": rule_data_list[61],
    "CoP Dead Dunes - Pride And Greed I CoP Quest (3)": rule_data_list[61],
    "CoP Dead Dunes - Pride And Greed II CoP Quest (1)": rule_data_list[78],
    "CoP Dead Dunes - Pride And Greed II CoP Quest (2)": rule_data_list[78],
    "CoP Dead Dunes - Pride And Greed II CoP Quest (3)": rule_data_list[78],
    "CoP Dead Dunes - Pride And Greed III CoP Quest (1)": rule_data_list[79],
    "CoP Dead Dunes - Pride And Greed III CoP Quest (2)": rule_data_list[79],
    "CoP Dead Dunes - Pride And Greed III CoP Quest (3)": rule_data_list[79],
    "CoP Luxerion - Revenge Is Sweet CoP Quest (1)": rule_data_list[80],
    "CoP Luxerion - Revenge Is Sweet CoP Quest (2)": rule_data_list[80],
    "CoP Luxerion - Gift of Gratitude CoP Quest (1)": rule_data_list[80],
    "CoP Luxerion - Gift of Gratitude CoP Quest (2)": rule_data_list[80],
    "CoP Luxerion - Gift of Gratitude CoP Quest (3)": rule_data_list[80],
    "CoP Luxerion - A Song for God CoP Quest (1)": rule_data_list[61],
    "CoP Luxerion - A Song for God CoP Quest (2)": rule_data_list[61],
    "CoP Luxerion - A Song for God CoP Quest (3)": rule_data_list[61],
    "CoP Luxerion - Slay the Machine CoP Quest (1)": rule_data_list[61],
    "CoP Luxerion - Slay the Machine CoP Quest (2)": rule_data_list[61],
    "CoP Luxerion - Enchanted Brush CoP Quest (1)": rule_data_list[81],
    "CoP Luxerion - Enchanted Brush CoP Quest (2)": rule_data_list[81],
    "CoP Luxerion - Enchanted Brush CoP Quest (3)": rule_data_list[81],
    "CoP Luxerion - Heretics' Beasts CoP Quest (1)": rule_data_list[82],
    "CoP Luxerion - Heretics' Beasts CoP Quest (2)": rule_data_list[82],
    "CoP Luxerion - Heretics' Beasts CoP Quest (3)": rule_data_list[82],
    "CoP Luxerion - Grave of a Bounty Hunter CoP Quest (1)": rule_data_list[63],
    "CoP Luxerion - Grave of a Bounty Hunter CoP Quest (2)": rule_data_list[63],
    "CoP Luxerion - Grave of a Bounty Hunter CoP Quest (3)": rule_data_list[63],
    "CoP Luxerion - Inventive Seamstress CoP Quest (1)": rule_data_list[80],
    "CoP Luxerion - Inventive Seamstress CoP Quest (2)": rule_data_list[80],
    "CoP Luxerion - Puppeteer's Lament CoP Quest (1)": rule_data_list[63],
    "CoP Luxerion - Puppeteer's Lament CoP Quest (2)": rule_data_list[63],
    "CoP Luxerion - Puppeteer's Lament CoP Quest (3)": rule_data_list[63],
    "CoP Luxerion - Revenge has Teeth CoP Quest (1)": rule_data_list[63],
    "CoP Luxerion - Revenge has Teeth CoP Quest (2)": rule_data_list[63],
    "CoP Luxerion - Night Patrol CoP Quest (1)": rule_data_list[83],
    "CoP Luxerion - Night Patrol CoP Quest (2)": rule_data_list[83],
    "CoP Luxerion - Night Patrol CoP Quest (3)": rule_data_list[83],
    "CoP Luxerion - Trapped CoP Quest (1)": rule_data_list[84],
    "CoP Luxerion - Trapped CoP Quest (2)": rule_data_list[84],
    "CoP Luxerion - Trapped CoP Quest (3)": rule_data_list[84],
    "CoP Luxerion - Trapped CoP Quest (4)": rule_data_list[84],
    "CoP Luxerion - Mythical Badge CoP Quest (1)": rule_data_list[85],
    "CoP Luxerion - Mythical Badge CoP Quest (2)": rule_data_list[85],
    "CoP Luxerion - Mythical Badge CoP Quest (3)": rule_data_list[85],
    "CoP Wildlands - Sun Flower CoP Quest (1)": rule_data_list[60],
    "CoP Wildlands - Sun Flower CoP Quest (2)": rule_data_list[60],
    "CoP Wildlands - Moon Flower CoP Quest (1)": rule_data_list[60],
    "CoP Wildlands - Moon Flower CoP Quest (2)": rule_data_list[60],
    "CoP Wildlands - Moon Flower CoP Quest (3)": rule_data_list[60],
    "CoP Wildlands - Secret of the Chocoborel CoP Quest (1)": rule_data_list[61],
    "CoP Wildlands - Secret of the Chocoborel CoP Quest (2)": rule_data_list[61],
    "CoP Wildlands - Secret of the Chocoborel CoP Quest (3)": rule_data_list[61],
    "CoP Wildlands - Wildlands In Danger! CoP Quest (1)": rule_data_list[86],
    "CoP Wildlands - Wildlands In Danger! CoP Quest (2)": rule_data_list[86],
    "CoP Wildlands - Wildlands In Danger! CoP Quest (3)": rule_data_list[86],
    "CoP Wildlands - Hunting the Hunter CoP Quest (1)": rule_data_list[87],
    "CoP Wildlands - Hunting the Hunter CoP Quest (2)": rule_data_list[87],
    "CoP Wildlands - Hunting the Hunter CoP Quest (3)": rule_data_list[87],
    "CoP Wildlands - Forget Me Not CoP Quest (1)": rule_data_list[60],
    "CoP Wildlands - Forget Me Not CoP Quest (2)": rule_data_list[60],
    "CoP Wildlands - Forget Me Not CoP Quest (3)": rule_data_list[60],
    "CoP Wildlands - A Word of Thanks CoP Quest (1)": rule_data_list[61],
    "CoP Wildlands - A Word of Thanks CoP Quest (2)": rule_data_list[61],
    "CoP Wildlands - A Word of Thanks CoP Quest (3)": rule_data_list[61],
    "CoP Wildlands - Fresh Fertilizer CoP Quest (1)": rule_data_list[88],
    "CoP Wildlands - Fresh Fertilizer CoP Quest (2)": rule_data_list[88],
    "CoP Wildlands - Fresh Fertilizer CoP Quest (3)": rule_data_list[88],
    "CoP Wildlands - For the Future CoP Quest (1)": rule_data_list[61],
    "CoP Wildlands - For the Future CoP Quest (2)": rule_data_list[61],
    "CoP Wildlands - For the Future CoP Quest (3)": rule_data_list[61],
    "CoP Wildlands - Dumpling Cook-Off CoP Quest (1)": rule_data_list[89],
    "CoP Wildlands - Dumpling Cook-Off CoP Quest (2)": rule_data_list[89],
    "CoP Wildlands - Dumpling Cook-Off CoP Quest (3)": rule_data_list[89],
    "CoP Wildlands - Brain Over Brawn CoP Quest (1)": rule_data_list[90],
    "CoP Wildlands - Brain Over Brawn CoP Quest (2)": rule_data_list[90],
    "CoP Wildlands - Brain Over Brawn CoP Quest (3)": rule_data_list[90],
    "CoP Wildlands - Hunter's Challenge CoP Quest (1)": rule_data_list[61],
    "CoP Wildlands - Hunter's Challenge CoP Quest (2)": rule_data_list[61],
    "CoP Wildlands - Hunter's Challenge CoP Quest (3)": rule_data_list[61],
    "CoP Wildlands - A Secret Wish CoP Quest (1)": rule_data_list[91],
    "CoP Wildlands - A Secret Wish CoP Quest (2)": rule_data_list[91],
    "CoP Wildlands - A Secret Wish CoP Quest (3)": rule_data_list[91],
    "CoP Wildlands - Moghan's Plea CoP Quest (1)": rule_data_list[37],
    "CoP Wildlands - Moghan's Plea CoP Quest (2)": rule_data_list[37],
    "CoP Wildlands - Moghan's Plea CoP Quest (3)": rule_data_list[37],
    "CoP Wildlands - What's in a Brew? CoP Quest (1)": rule_data_list[92],
    "CoP Wildlands - What's in a Brew? CoP Quest (2)": rule_data_list[92],
    "CoP Wildlands - What's in a Brew? CoP Quest (3)": rule_data_list[92],
    "CoP Wildlands - What's in a Brew? CoP Quest (4)": rule_data_list[92],
    "CoP Wildlands - A Prayer to a Goddess CoP Quest (1)": rule_data_list[93],
    "CoP Wildlands - A Prayer to a Goddess CoP Quest (2)": rule_data_list[93],
    "CoP Wildlands - A Prayer to a Goddess CoP Quest (3)": rule_data_list[93],
    "CoP Wildlands - Gatekeeper's Curiosity CoP Quest (1)": rule_data_list[63],
    "CoP Wildlands - Gatekeeper's Curiosity CoP Quest (2)": rule_data_list[63],
    "CoP Wildlands - Echoes of a Drum CoP Quest (1)": rule_data_list[61],
    "CoP Wildlands - Echoes of a Drum CoP Quest (2)": rule_data_list[61],
    "CoP Wildlands - Echoes of a Drum CoP Quest (3)": rule_data_list[61],
    "CoP Wildlands - A Voice From Below CoP Quest (1)": rule_data_list[61],
    "CoP Wildlands - A Voice From Below CoP Quest (2)": rule_data_list[61],
    "CoP Wildlands - A Voice From Below CoP Quest (3)": rule_data_list[61],
    "CoP Wildlands - Chocobo Chow CoP Quest (1)": rule_data_list[94],
    "CoP Wildlands - Chocobo Chow CoP Quest (2)": rule_data_list[94],
    "CoP Wildlands - Chocobo Chow CoP Quest (3)": rule_data_list[94],
    "CoP Wildlands - Sylkis Secrets CoP Quest (1)": rule_data_list[95],
    "CoP Wildlands - Sylkis Secrets CoP Quest (2)": rule_data_list[95],
    "CoP Wildlands - Sylkis Secrets CoP Quest (3)": rule_data_list[95],
    "CoP Wildlands - Digging Mole CoP Quest (1)": rule_data_list[96],
    "CoP Wildlands - Digging Mole CoP Quest (2)": rule_data_list[96],
    "CoP Wildlands - Digging Mole CoP Quest (3)": rule_data_list[96],
    "CoP Wildlands - Two Together CoP Quest (1)": rule_data_list[97],
    "CoP Wildlands - Two Together CoP Quest (2)": rule_data_list[97],
    "CoP Wildlands - Two Together CoP Quest (3)": rule_data_list[97],
    "CoP Wildlands - Emergency Treatment CoP Quest (1)": rule_data_list[31],
    "CoP Wildlands - Emergency Treatment CoP Quest (2)": rule_data_list[31],
    "CoP Wildlands - Emergency Treatment CoP Quest (3)": rule_data_list[31],
    "CoP Wildlands - Moogle Gourmand CoP Quest (1)": rule_data_list[98],
    "CoP Wildlands - Moogle Gourmand CoP Quest (2)": rule_data_list[98],
    "CoP Wildlands - Moogle Gourmand CoP Quest (3)": rule_data_list[98],
    "CoP Yusnaan - Secret Machine CoP Quest (1)": rule_data_list[60],
    "CoP Yusnaan - Secret Machine CoP Quest (2)": rule_data_list[60],
    "CoP Yusnaan - Soulful Horn CoP Quest (1)": rule_data_list[14],
    "CoP Yusnaan - Soulful Horn CoP Quest (2)": rule_data_list[14],
    "CoP Yusnaan - Soulful Horn CoP Quest (3)": rule_data_list[14],
    "CoP Yusnaan - A Dangerous Cocktail CoP Quest (1)": rule_data_list[61],
    "CoP Yusnaan - A Dangerous Cocktail CoP Quest (2)": rule_data_list[61],
    "CoP Yusnaan - Source of Inspiration CoP Quest (1)": rule_data_list[63],
    "CoP Yusnaan - Source of Inspiration CoP Quest (2)": rule_data_list[63],
    "CoP Yusnaan - Youth Potion CoP Quest (1)": rule_data_list[90],
    "CoP Yusnaan - Youth Potion CoP Quest (2)": rule_data_list[90],
    "CoP Yusnaan - Youth Potion CoP Quest (3)": rule_data_list[90],
    "CoP Yusnaan - Beast Summoner CoP Quest (1)": rule_data_list[99],
    "CoP Yusnaan - Beast Summoner CoP Quest (2)": rule_data_list[99],
    "CoP Yusnaan - Beast Summoner CoP Quest (3)": rule_data_list[99],
    "CoP Yusnaan - What Seekers Seek CoP Quest (1)": rule_data_list[100],
    "CoP Yusnaan - What Seekers Seek CoP Quest (2)": rule_data_list[100],
    "CoP Yusnaan - What Seekers Seek CoP Quest (3)": rule_data_list[100],
    "CoP Yusnaan - True Colors CoP Quest (1)": rule_data_list[63],
    "CoP Yusnaan - True Colors CoP Quest (2)": rule_data_list[63],
    "CoP Yusnaan - True Colors CoP Quest (3)": rule_data_list[63],
    "CoP Yusnaan - Ultimate Craving CoP Quest (1)": rule_data_list[101],
    "CoP Yusnaan - Ultimate Craving CoP Quest (2)": rule_data_list[101],
    "CoP Yusnaan - Ultimate Craving CoP Quest (3)": rule_data_list[101],
    "CoP Yusnaan - Ultimate Craving CoP Quest (4)": rule_data_list[101],
    "CoP Yusnaan - Spell for Spell CoP Quest (1)": rule_data_list[90],
    "CoP Yusnaan - Spell for Spell CoP Quest (2)": rule_data_list[90],
    "CoP Yusnaan - Spell for Spell CoP Quest (3)": rule_data_list[90],
    "CoP Yusnaan - Unfired Firework CoP Quest (1)": rule_data_list[49],
    "CoP Yusnaan - Unfired Firework CoP Quest (2)": rule_data_list[49],
    "CoP Yusnaan - Unfired Firework CoP Quest (3)": rule_data_list[49],
    "CoP Yusnaan - Time Doesn't Heal CoP Quest (1)": rule_data_list[102],
    "CoP Yusnaan - Time Doesn't Heal CoP Quest (2)": rule_data_list[102],
    "CoP Yusnaan - Time Doesn't Heal CoP Quest (3)": rule_data_list[102],
    "CoP Yusnaan - A Man for a Chocobo Girl CoP Quest (1)": rule_data_list[103],
    "CoP Yusnaan - A Man for a Chocobo Girl CoP Quest (2)": rule_data_list[103],
    "CoP Yusnaan - A Man for a Chocobo Girl CoP Quest (3)": rule_data_list[103],
    "CoP Yusnaan - Rebuilding CoP Quest (1)": rule_data_list[49],
    "CoP Yusnaan - Rebuilding CoP Quest (2)": rule_data_list[49],
    "CoP Global - Global: Key To Her Heart CoP Quest (1)": rule_data_list[104],
    "CoP Global - Global: Key To Her Heart CoP Quest (2)": rule_data_list[104],
    "CoP Global - Global: Key To Her Heart CoP Quest (3)": rule_data_list[104],
    "CoP Global - Global: Roadworks I CoP Quest (1)": rule_data_list[105],
    "CoP Global - Global: Roadworks I CoP Quest (2)": rule_data_list[105],
    "CoP Global - Global: Roadworks I CoP Quest (3)": rule_data_list[105],
    "CoP Global - Global: Roadworks II CoP Quest (1)": rule_data_list[106],
    "CoP Global - Global: Roadworks II CoP Quest (2)": rule_data_list[106],
    "CoP Global - Global: Roadworks II CoP Quest (3)": rule_data_list[106],
    "CoP Global - Global: Roadworks III CoP Quest (1)": rule_data_list[107],
    "CoP Global - Global: Roadworks III CoP Quest (2)": rule_data_list[107],
    "CoP Global - Global: Roadworks III CoP Quest (3)": rule_data_list[107],
    "CoP Global - Global: A Girl's Challenge CoP Quest (1)": rule_data_list[108],
    "CoP Global - Global: A Girl's Challenge CoP Quest (2)": rule_data_list[108],
    "CoP Global - Global: What's Left Behind CoP Quest (1)": rule_data_list[109],
    "CoP Global - Global: What's Left Behind CoP Quest (2)": rule_data_list[109],
    "CoP Global - Global: Seeing The Dawn CoP Quest (1)": rule_data_list[110],
    "CoP Global - Global: Seeing The Dawn CoP Quest (2)": rule_data_list[110],
    "CoP Global - Global: Staying Sharp CoP Quest (1)": rule_data_list[111],
    "CoP Global - Global: Staying Sharp CoP Quest (2)": rule_data_list[111],
    "CoP Global - Global: Where Moogles Be CoP Quest (1)": rule_data_list[112],
    "CoP Global - Global: Where Moogles Be CoP Quest (2)": rule_data_list[112],
    "CoP Global - Global: Fading Prayer CoP Quest (1)": rule_data_list[113],
    "CoP Global - Global: Fading Prayer CoP Quest (2)": rule_data_list[113],
    "CoP Global - Global: Forbidden Tome CoP Quest (1)": rule_data_list[114],
    "CoP Global - Global: Forbidden Tome CoP Quest (2)": rule_data_list[114],
    "CoP Global - Global: Shoot For The Sky CoP Quest (1)": rule_data_list[115],
    "CoP Global - Global: Shoot For The Sky CoP Quest (2)": rule_data_list[115],
    "CoP Global - Global: Shoot For The Sky CoP Quest (3)": rule_data_list[115],
    "CoP Global - Global: Digging Mysteries CoP Quest (1)": rule_data_list[116],
    "CoP Global - Global: Digging Mysteries CoP Quest (2)": rule_data_list[116],
    "CoP Global - Global: Digging Mysteries CoP Quest (3)": rule_data_list[116],
    "Soul Seeds/Unappraised - 10 Soul Seeds": rule_data_list[117],
    "Soul Seeds/Unappraised - 20 Soul Seeds": rule_data_list[117],
    "Soul Seeds/Unappraised - 30 Soul Seeds": rule_data_list[117],
    "Soul Seeds/Unappraised - 40 Soul Seeds": rule_data_list[117],
    "Soul Seeds/Unappraised - 50 Soul Seeds": rule_data_list[117],
    "Soul Seeds/Unappraised - Soul Seeds Fragment of Radiance": rule_data_list[118],
    "Soul Seeds/Unappraised - 1 Unappraised": rule_data_list[5],
    "Soul Seeds/Unappraised - 5 Unappraised": rule_data_list[5],
    "Soul Seeds/Unappraised - 10 Unappraised": rule_data_list[5],
    "Soul Seeds/Unappraised - 20 Unappraised": rule_data_list[5],
    "Soul Seeds/Unappraised - 50 Unappraised": rule_data_list[5],
    "Ultimate Lair - Hoplite Omega Drop (1F)": rule_data_list[0],
    "Ultimate Lair - Niblet Omega Drop (2F)": rule_data_list[0],
    "Ultimate Lair - Zaltys Omega Drop (3F)": rule_data_list[0],
    "Ultimate Lair - Gaunt Omega Drop (4F)": rule_data_list[0],
    "Ultimate Lair - Gremlin Omega Drop (5F)": rule_data_list[0],
    "Ultimate Lair - Dreadnought Omega Drop (6F)": rule_data_list[0],
    "Ultimate Lair - Gorgonopsid Omega Drop (7F)": rule_data_list[0],
    "Ultimate Lair - Goblot Omega Drop (8F)": rule_data_list[0],
    "Ultimate Lair - Gurangatch Omega Drop (9F)": rule_data_list[0],
    "Ultimate Lair - Ectopudding Omega Drop (10F)": rule_data_list[0],
    "Ultimate Lair - Miniflan Omega Drop (11F)": rule_data_list[0],
    "Ultimate Lair - Aster Protoflorian Omega Drop (12F)": rule_data_list[0],
    "Ultimate Lair - Schrodinger Omega Drop (13F)": rule_data_list[0],
    "Ultimate Lair - Goblin Omega Drop (14F)": rule_data_list[0],
    "Ultimate Lair - Reaver Omega Drop (15F)": rule_data_list[0],
    "Ultimate Lair - Meonekton Omega Drop (16F)": rule_data_list[0],
    "Ultimate Lair - Cactuar Omega Drop (17F)": rule_data_list[0],
    "Ultimate Lair - Triffid Omega Drop (18F)": rule_data_list[0],
    "Ultimate Lair - Cyclops Omega Drop (19F)": rule_data_list[0],
    "Ultimate Lair - Skeleton Omega Drop (20F)": rule_data_list[0],
    "Ultimate Lair - Desert Sahagin Omega Drop (21F)": rule_data_list[0],
    "Ultimate Lair - Earth Eater Omega Drop (22F)": rule_data_list[0],
    "Ultimate Lair - Skata'ne Omega Drop (23F)": rule_data_list[0],
    "Ultimate Lair - Hanuman Omega Drop (24F)": rule_data_list[0],
    "Ultimate Lair - Zomok Omega Drop (25F)": rule_data_list[0],
    "Ultimate Lair - Dryad Omega Drop (26F)": rule_data_list[0],
    "Ultimate Lair - Rafflesia Omega Drop (27F)": rule_data_list[0],
    "Ultimate Lair - Chocobo Eater Omega Drop (28F)": rule_data_list[0],
    "Ultimate Lair - Ultimate Lair Floor 29": rule_data_list[0],
    "Ultimate Lair - Ultimate Lair Floor 30": rule_data_list[0],
    "Ultimate Lair - Ultimate Lair Floor 31": rule_data_list[0],
    "Ultimate Lair - Ultimate Lair Floor 32": rule_data_list[0],
    "Ultimate Lair - Ultimate Lair Boss Drop": rule_data_list[0],
    "Ultimate Lair - Ultimate Lair Boss Reward": rule_data_list[0],
    "Final Day - Arcangeli Omega Drop": rule_data_list[69],
    "Final Day - Sugriva Omega Drop": rule_data_list[69],
    "Final Day - Chimera Omega Drop": rule_data_list[69],
    "Final Day - Final Day Altar Of Salvation": rule_data_list[69],
    "Final Day - Final Day Altar Of Judgment": rule_data_list[69],
    "Final Day - Final Day Altar Of Atonement": rule_data_list[69],
    "Final Day - Final Day Altar Of Birth": rule_data_list[69],
    "Final Day - Final Day Temple Of Light (1)": rule_data_list[69],
    "Final Day - Final Day Temple Of Light (2)": rule_data_list[69],
    "Final Day - Final Day Temple Of Light (3)": rule_data_list[69],
    "Final Day - Final Day Ultima Weapon": rule_data_list[69],
    "Final Day - Final Day Ultima Shield": rule_data_list[69],
    "Dead Dunes - Cactair Fragment of Kindness": rule_data_list[0],
    "Dead Dunes - Goblots Arithmometer": rule_data_list[0],
    "Dead Dunes - Aeronite Monster Flesh": rule_data_list[65],
    "Luxerion - Zomok Cursed Dragon Claw": rule_data_list[0],
    "Yusnaan - Gremlins Music Satchel": rule_data_list[0],
    "Yusnaan - Schrodinger Civet Musk": rule_data_list[0],
    "Ark Day 0 Event (1)": rule_data_list[0],
    "Ark Day 1 Event (1)": rule_data_list[0],
    "Ark Day 2 Event (1)": rule_data_list[60],
    "Ark Day 3 Event (1)": rule_data_list[14],
    "Ark Day 4 Event (1)": rule_data_list[61],
    "Ark Day 5 Event (1)": rule_data_list[62],
    "Ark Day 6 Event (1)": rule_data_list[63],
    "Main Quest 4 Event (1)": rule_data_list[119],
    "Main Quest 4 Event (2)": rule_data_list[119],
    "Main Quest 1 Event (1)": rule_data_list[120],
    "Main Quest 1 Event (2)": rule_data_list[120],
    "Main Quest 3 Event (1)": rule_data_list[121],
    "Main Quest 3 Event (2)": rule_data_list[121],
    "Main Quest 2 Event (1)": rule_data_list[122],
    "Main Quest 2 Event (2)": rule_data_list[122],
    "Main Quest 5 Event (1)": rule_data_list[123],
    "Main Quest 5 Event (2)": rule_data_list[123],
    "The Things She Lost Quest Event (1)": rule_data_list[17],
    "Where Are You, Holmes? Quest Event (1)": rule_data_list[0],
    "Like Clockwork Quest Event (1)": rule_data_list[12],
    "Dying Wish Quest Event (1)": rule_data_list[18],
    "Suspicious Spheres Quest Event (1)": rule_data_list[19],
    "Born From Chaos Quest Event (1)": rule_data_list[20],
    "Soul Seeds Quest Event (1)": rule_data_list[15],
    "Faster Than Lightning Quest Event (1)": rule_data_list[15],
    "Treasured Ball Quest Event (1)": rule_data_list[21],
    "The Angel's Tears Quest Event (1)": rule_data_list[15],
    "The Saint's Stone Quest Event (1)": rule_data_list[13],
    "Whither Faith Quest Event (1)": rule_data_list[0],
    "The Avid Reader Quest Event (1)": rule_data_list[13],
    "Buried Passion Quest Event (1)": rule_data_list[24],
    "The Girl Who Cried Wolf Quest Event (1)": rule_data_list[13],
    "Stuck in a Gem Quest Event (1)": rule_data_list[0],
    "Get the Girl Quest Event (1)": rule_data_list[13],
    "A Rose By Any Other Name Quest Event (1)": rule_data_list[25],
    "Voices from the Grave Quest Event (1)": rule_data_list[13],
    "To Save the Sinless Quest Event (1)": rule_data_list[26],
    "The Life of a Machine Quest Event (1)": rule_data_list[3],
    "Old Rivals Quest Event (1)": rule_data_list[4],
    "His Wife's Dream Quest Event (1)": rule_data_list[4],
    "Tool of the Trade Quest Event (1)": rule_data_list[5],
    "Adonis's Audition Quest Event (1)": rule_data_list[6],
    "What Rough Beast Slouches Quest Event (1)": rule_data_list[7],
    "Skeletons In The Closet Quest Event (1)": rule_data_list[8],
    "Last One Standing Quest Event (1)": rule_data_list[0],
    "A Father's Request Quest Event (1)": rule_data_list[28],
    "The Hunter's Challenge Quest Event (1)": rule_data_list[29],
    "A Final Cure Quest Event (1)": rule_data_list[28],
    "Fuzzy Search Quest Event (1)": rule_data_list[30],
    "Round 'em Up Quest Event (1)": rule_data_list[31],
    "Chocobo Cheer Quest Event (1)": rule_data_list[31],
    "Peace and Quiet, Kupo Quest Event (1)": rule_data_list[0],
    "Saving an Angel Quest Event (1)": rule_data_list[28],
    "Omega Point Quest Event (1)": rule_data_list[32],
    "The Old Man and the Field Quest Event (1)": rule_data_list[33],
    "Land of our Forebears Quest Event (1)": rule_data_list[34],
    "A Taste of the Past Quest Event (1)": rule_data_list[35],
    "Dog, Doctor and Assistant Quest Event (1)": rule_data_list[31],
    "The Right Stuff Quest Event (1)": rule_data_list[28],
    "The Secret Lives of Sheep Quest Event (1)": rule_data_list[30],
    "Where Are You, Moogle? Quest Event (1)": rule_data_list[37],
    "Mercy of a Goddess Quest Event (1)": rule_data_list[38],
    "The Grail of Valhalla Quest Event (1)": rule_data_list[39],
    "To Live in Chaos Quest Event (1)": rule_data_list[40],
    "Killing Time Quest Event (1)": rule_data_list[27],
    "Matchmaker Quest Event (1)": rule_data_list[41],
    "Mother and Daughter Quest Event (1)": rule_data_list[42],
    "Fireworks in a Bottle Quest Event (1)": rule_data_list[44],
    "The Fighting Actress Quest Event (1)": rule_data_list[44],
    "Songless Diva Quest Event (1)": rule_data_list[51],
    "Stolen Things Quest Event (1)": rule_data_list[52],
    "Fireworks for a Steal Quest Event (1)": rule_data_list[44],
    "A Testing Proposition Quest Event (1)": rule_data_list[0],
    "Last Date Quest Event (1)": rule_data_list[49],
    "Free Will Quest Event (1)": rule_data_list[0],
    "Friends Forever Quest Event (1)": rule_data_list[49],
    "Family Food Quest Event (1)": rule_data_list[53],
    "Tanbam's Taboo Quest Event (1)": rule_data_list[49],
    "Play It for Me Quest Event (1)": rule_data_list[54],
    "Adoring Adornments Quest Event (1)": rule_data_list[55],
    "Adoring Candice Quest Event (1)": rule_data_list[56],
    "Death Safari Quest Event (1)": rule_data_list[44],
    "Death Game Quest Event (1)": rule_data_list[57],
    "Main Quest 1-1 Event (1)": rule_data_list[0],
    "Main Quest 1-2 Event (1)": rule_data_list[80],
    "Main Quest 1-3 Event (1)": rule_data_list[15],
    "Main Quest 1-4 Event (1)": rule_data_list[11],
    "Main Quest 2-1 cyclops Event (1)": rule_data_list[124],
    "Main Quest 2-1 Event (1)": rule_data_list[125],
    "Main Quest 2-2 Event (1)": rule_data_list[50],
    "Main Quest 3-1 Event (1)": rule_data_list[0],
    "Main Quest 3-2 Event (1)": rule_data_list[126],
    "Main Quest 3-3 Flight Event (1)": rule_data_list[31],
    "Main Quest 4-1 Event (1)": rule_data_list[0],
    "Main Quest 4-2 Event (1)": rule_data_list[6],
    "Main Quest 4-3 Event (1)": rule_data_list[127],
    "Main Quest 4-4 First Tablet placed Event (1)": rule_data_list[128],
    "Main Quest 4-4 Event (1)": rule_data_list[129],
    "Main Quest 5 start Event (1)": rule_data_list[130],
    "Victory Event (1)": rule_data_list[131],
    "Banned Goods Event (1)": rule_data_list[60],
    "Miracle Vintage Event (1)": rule_data_list[62],
    "For My Child Event (1)": rule_data_list[61],
    "Heightened Security Event (1)": rule_data_list[62],
    "Climbing the Ranks I Event (1)": rule_data_list[61],
    "Climbing the Ranks II Event (1)": rule_data_list[73],
    "Flower in the Sands Event (1)": rule_data_list[60],
    "Biologically Speaking Event (1)": rule_data_list[60],
    "Lucky Charm Event (1)": rule_data_list[0],
    "Pride and Greed I Event (1)": rule_data_list[61],
    "Pride and Greed II Event (1)": rule_data_list[78],
    "Pride and Greed III Event (1)": rule_data_list[79],
    "Revenge is Sweet Event (1)": rule_data_list[0],
    "Gift of Gratitude Event (1)": rule_data_list[0],
    "A Song for God Event (1)": rule_data_list[61],
    "Grave of a Bounty Hunter Event (1)": rule_data_list[63],
    "Inventive Seamstress Event (1)": rule_data_list[80],
    "Puppeteer's Lament Event (1)": rule_data_list[63],
    "Slay the Machine Event (1)": rule_data_list[61],
    "Revenge Has Teeth Event (1)": rule_data_list[63],
    "Sun Flower Event (1)": rule_data_list[60],
    "Moon Flower Event (1)": rule_data_list[60],
    "Forget Me Not Event (1)": rule_data_list[60],
    "A Word of Thanks Event (1)": rule_data_list[61],
    "Fresh Fertilizer Event (1)": rule_data_list[88],
    "For the Future Event (1)": rule_data_list[61],
    "Echoes of a Drum Event (1)": rule_data_list[61],
    "A Voice from Below Event (1)": rule_data_list[61],
    "Brain Over Brawn Event (1)": rule_data_list[90],
    "Hunter's Challenge Event (1)": rule_data_list[61],
    "Moghan's Plea Event (1)": rule_data_list[37],
    "Gatekeeper's Curiosity Event (1)": rule_data_list[63],
    "Chocobo Chow Event (1)": rule_data_list[94],
    "Secret Machine Event (1)": rule_data_list[60],
    "Soulful Horn Event (1)": rule_data_list[14],
    "A Dangerous Cocktail Event (1)": rule_data_list[61],
    "A Man for a Chocobo Girl Event (1)": rule_data_list[103],
    "Source of Inspiration Event (1)": rule_data_list[63],
    "True Colors Event (1)": rule_data_list[63],
    "Youth Potion Event (1)": rule_data_list[90],
    "Spell for Spell Event (1)": rule_data_list[90],
    "0-1 Hint Event (1)": rule_data_list[0],
    "1-1 Hint Event (1)": rule_data_list[80],
    "1-2 Hint Event (1)": rule_data_list[15],
    "1-3 Hint Event (1)": rule_data_list[11],
    "1-4 Hint Event (1)": rule_data_list[12],
    "1-5 Hint Event (1)": rule_data_list[13],
    "2-1 Hint Event (1)": rule_data_list[132],
    "2-2 Hint Event (1)": rule_data_list[133],
    "2-3 Hint Event (1)": rule_data_list[134],
    "3-1 Hint Event (1)": rule_data_list[135],
    "3-2 Hint Event (1)": rule_data_list[136],
    "3-3 Hint Event (1)": rule_data_list[137],
    "4-1 Hint Event (1)": rule_data_list[6],
    "4-2 Hint Event (1)": rule_data_list[127],
    "4-3 Hint Event (1)": rule_data_list[3],
    "4-4 Hint Event (1)": rule_data_list[138],
    "4-5 Hint Event (1)": rule_data_list[139],
    "5-1 Hint Event (1)": rule_data_list[140],
    "5-2 Hint Event (1)": rule_data_list[141],
    "5-3 Hint Event (1)": rule_data_list[142],
    "5-4 Hint Event (1)": rule_data_list[143],
    "5-5 Hint Event (1)": rule_data_list[141],
    "5-6 Hint Event (1)": rule_data_list[0],
}

item_rule_data_table: Dict[str, Callable[[Item], bool]] = {
    "Ark - Initial 3rd Garb (1)": lambda item: item_is_category(item.name, "Garb"),
    "Ark - Initial 3rd Garb (2)": lambda item: item_is_category(item.name, "Weapon"),
    "Ark - Initial 3rd Garb (3)": lambda item: item_is_category(item.name, "Shield"),
}

entrance_rule_data_table: Dict[Tuple[str, str], Callable[[CollectionState, int], bool]] = {
    ("Initial", "Ark"): rule_data_list[0],
    ("Luxerion", "Dead Dunes"): rule_data_list[14],
    ("Ark", "Luxerion"): rule_data_list[0],
    ("Luxerion", "Wildlands"): rule_data_list[14],
    ("Luxerion", "Yusnaan"): rule_data_list[14],
    ("Dead Dunes", "CoP Dead Dunes"): rule_data_list[14],
    ("Luxerion", "CoP Luxerion"): rule_data_list[14],
    ("Wildlands", "CoP Wildlands"): rule_data_list[14],
    ("Yusnaan", "CoP Yusnaan"): rule_data_list[14],
    ("Ark", "CoP Global"): rule_data_list[14],
    ("Dead Dunes", "Soul Seeds/Unappraised"): rule_data_list[14],
    ("Ark", "Ultimate Lair"): rule_data_list[61],
    ("Ark", "Final Day"): rule_data_list[131],
}
