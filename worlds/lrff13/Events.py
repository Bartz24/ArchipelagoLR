from typing import Dict, NamedTuple


class LRFF13EventData(NamedTuple):
    region: str
    item: str
    traits: list = []


event_data_table: Dict[str, LRFF13EventData] = {
    "Ark Day 0 Event (1)": LRFF13EventData(
        region="Ark",
        item="",
        traits=["Day", "Fake"]
    ),
    "Ark Day 1 Event (1)": LRFF13EventData(
        region="Ark",
        item="Day",
        traits=["Day", "Fake"]
    ),
    "Ark Day 2 Event (1)": LRFF13EventData(
        region="Ark",
        item="Day",
        traits=["Fake"]
    ),
    "Ark Day 3 Event (1)": LRFF13EventData(
        region="Ark",
        item="Day",
        traits=["Fake"]
    ),
    "Ark Day 4 Event (1)": LRFF13EventData(
        region="Ark",
        item="Day",
        traits=["NoCascade", "Fake"]
    ),
    "Ark Day 5 Event (1)": LRFF13EventData(
        region="Ark",
        item="Day",
        traits=["NoCascade", "Fake"]
    ),
    "Ark Day 6 Event (1)": LRFF13EventData(
        region="Ark",
        item="Day",
        traits=["NoCascade", "Fake"]
    ),
    "Main Quest 4 Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="MQ4",
        traits=["Main", "Fake"]
    ),
    "Main Quest 4 Event (2)": LRFF13EventData(
        region="Dead Dunes",
        item="MQDone",
        traits=["Main", "Fake"]
    ),
    "Main Quest 1 Event (1)": LRFF13EventData(
        region="Luxerion",
        item="MQ1",
        traits=["Main", "Fake"]
    ),
    "Main Quest 1 Event (2)": LRFF13EventData(
        region="Luxerion",
        item="MQDone",
        traits=["Main", "Fake"]
    ),
    "Main Quest 3 Event (1)": LRFF13EventData(
        region="Wildlands",
        item="MQ3",
        traits=["Main", "Fake"]
    ),
    "Main Quest 3 Event (2)": LRFF13EventData(
        region="Wildlands",
        item="MQDone",
        traits=["Main", "Fake"]
    ),
    "Main Quest 2 Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="MQ2",
        traits=["Main", "Fake"]
    ),
    "Main Quest 2 Event (2)": LRFF13EventData(
        region="Yusnaan",
        item="MQDone",
        traits=["Main", "Fake"]
    ),
    "Main Quest 5 Event (1)": LRFF13EventData(
        region="Wildlands",
        item="MQ5",
        traits=["Main", "Fake"]
    ),
    "Main Quest 5 Event (2)": LRFF13EventData(
        region="Wildlands",
        item="MQDone",
        traits=["Main", "Fake"]
    ),
    "The Things She Lost Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Where Are You, Holmes? Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Like Clockwork Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Dying Wish Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Suspicious Spheres Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Born From Chaos Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Soul Seeds Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Faster Than Lightning Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Treasured Ball Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "The Angel's Tears Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "The Saint's Stone Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="Q_Saint",
        traits=["Fake"]
    ),
    "Whither Faith Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "The Avid Reader Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Buried Passion Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="Q_BuriedPassion",
        traits=["Fake"]
    ),
    "The Girl Who Cried Wolf Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Stuck in a Gem Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Get the Girl Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "A Rose By Any Other Name Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "Voices from the Grave Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "To Save the Sinless Quest Event (1)": LRFF13EventData(
        region="Luxerion",
        item="",
        traits=["Fake"]
    ),
    "The Life of a Machine Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="",
        traits=["Fake"]
    ),
    "Old Rivals Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="",
        traits=["Fake"]
    ),
    "His Wife's Dream Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="Q_WifesDream",
        traits=["Fake"]
    ),
    "Tool of the Trade Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="",
        traits=["Fake"]
    ),
    "Adonis's Audition Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="",
        traits=["Fake"]
    ),
    "What Rough Beast Slouches Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="",
        traits=["Fake"]
    ),
    "Skeletons In The Closet Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="",
        traits=["Fake"]
    ),
    "Last One Standing Quest Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="",
        traits=["Fake"]
    ),
    "A Father's Request Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_Father",
        traits=["Fake"]
    ),
    "The Hunter's Challenge Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_Hunter",
        traits=["Fake"]
    ),
    "A Final Cure Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_Cure",
        traits=["Fake"]
    ),
    "Fuzzy Search Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_FuzzySearch",
        traits=["Fake"]
    ),
    "Round 'em Up Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_RoundUp",
        traits=["Fake"]
    ),
    "Chocobo Cheer Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Peace and Quiet, Kupo Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_Peace",
        traits=["Fake"]
    ),
    "Saving an Angel Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Omega Point Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "The Old Man and the Field Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_OldMan",
        traits=["Fake"]
    ),
    "Land of our Forebears Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_Forebears",
        traits=["Fake"]
    ),
    "A Taste of the Past Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Dog, Doctor and Assistant Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_DDA",
        traits=["Fake"]
    ),
    "The Right Stuff Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="Q_RightStuff",
        traits=["Fake"]
    ),
    "The Secret Lives of Sheep Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Where Are You, Moogle? Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Mercy of a Goddess Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "The Grail of Valhalla Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "To Live in Chaos Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Killing Time Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Matchmaker Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Mother and Daughter Quest Event (1)": LRFF13EventData(
        region="Wildlands",
        item="",
        traits=["Fake"]
    ),
    "Fireworks in a Bottle Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "The Fighting Actress Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="Q_Actress",
        traits=["Fake"]
    ),
    "Songless Diva Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Stolen Things Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Fireworks for a Steal Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "A Testing Proposition Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Last Date Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Missable", "Fake"]
    ),
    "Free Will Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Friends Forever Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Family Food Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="Q_Food",
        traits=["Fake"]
    ),
    "Tanbam's Taboo Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Play It for Me Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Adoring Adornments Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="Q_Adorn",
        traits=["Grindy", "Fake"]
    ),
    "Adoring Candice Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Grindy", "Fake"]
    ),
    "Death Safari Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="Q_Death",
        traits=["Fake"]
    ),
    "Death Game Quest Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="",
        traits=["Fake"]
    ),
    "Main Quest 1-1 Event (1)": LRFF13EventData(
        region="Luxerion",
        item="MQ1",
        traits=["Main", "Fake"]
    ),
    "Main Quest 1-2 Event (1)": LRFF13EventData(
        region="Luxerion",
        item="MQ1",
        traits=["Main", "Fake"]
    ),
    "Main Quest 1-3 Event (1)": LRFF13EventData(
        region="Luxerion",
        item="MQ1",
        traits=["Main", "Fake"]
    ),
    "Main Quest 1-4 Event (1)": LRFF13EventData(
        region="Luxerion",
        item="MQ1",
        traits=["Main", "Fake"]
    ),
    "Main Quest 2-1 cyclops Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="MQ2",
        traits=["Main", "Fake"]
    ),
    "Main Quest 2-1 Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="MQ2",
        traits=["Main", "Fake"]
    ),
    "Main Quest 2-2 Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="MQ2",
        traits=["Main", "Fake"]
    ),
    "Main Quest 3-1 Event (1)": LRFF13EventData(
        region="Wildlands",
        item="MQ3",
        traits=["Main", "Fake"]
    ),
    "Main Quest 3-2 Event (1)": LRFF13EventData(
        region="Wildlands",
        item="MQ3",
        traits=["Main", "Fake"]
    ),
    "Main Quest 3-3 Flight Event (1)": LRFF13EventData(
        region="Wildlands",
        item="MQ3",
        traits=["Main", "Fake"]
    ),
    "Main Quest 4-1 Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="MQ4",
        traits=["Main", "Fake"]
    ),
    "Main Quest 4-2 Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="MQ4",
        traits=["Main", "Fake"]
    ),
    "Main Quest 4-3 Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="MQ4",
        traits=["Main", "Fake"]
    ),
    "Main Quest 4-4 First Tablet placed Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="MQ4",
        traits=["Main", "Fake"]
    ),
    "Main Quest 4-4 Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="MQ4",
        traits=["Main", "Fake"]
    ),
    "Main Quest 5 start Event (1)": LRFF13EventData(
        region="Wildlands",
        item="MQ5",
        traits=["Main", "Fake"]
    ),
    "Victory Event (1)": LRFF13EventData(
        region="Final Day",
        item="Victory",
        traits=["Missable", "Fake"]
    ),
    "Banned Goods Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Banned",
        traits=["CoP", "Fake"]
    ),
    "Miracle Vintage Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Miracle",
        traits=["CoP", "Fake"]
    ),
    "For My Child Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Child",
        traits=["CoP", "Fake"]
    ),
    "Heightened Security Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Security",
        traits=["CoP", "Fake"]
    ),
    "Climbing the Ranks I Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Ranks",
        traits=["CoP", "Fake"]
    ),
    "Climbing the Ranks II Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Ranks",
        traits=["CoP", "Fake"]
    ),
    "Flower in the Sands Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Flower",
        traits=["CoP", "Fake"]
    ),
    "Biologically Speaking Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Bio",
        traits=["CoP", "Fake"]
    ),
    "Lucky Charm Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Charm",
        traits=["CoP", "Fake"]
    ),
    "Pride and Greed I Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Pride",
        traits=["CoP", "Fake"]
    ),
    "Pride and Greed II Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Pride",
        traits=["CoP", "Fake"]
    ),
    "Pride and Greed III Event (1)": LRFF13EventData(
        region="CoP Dead Dunes",
        item="C_Pride",
        traits=["CoP", "Fake"]
    ),
    "Revenge is Sweet Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Revenge",
        traits=["CoP", "Fake"]
    ),
    "Gift of Gratitude Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Gratitude",
        traits=["CoP", "Fake"]
    ),
    "A Song for God Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Song",
        traits=["CoP", "Fake"]
    ),
    "Grave of a Bounty Hunter Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Grave",
        traits=["CoP", "Fake"]
    ),
    "Inventive Seamstress Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Inventive",
        traits=["CoP", "Fake"]
    ),
    "Puppeteer's Lament Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Puppet",
        traits=["CoP", "Fake"]
    ),
    "Slay the Machine Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Slay",
        traits=["CoP", "Fake"]
    ),
    "Revenge Has Teeth Event (1)": LRFF13EventData(
        region="CoP Luxerion",
        item="C_Teeth",
        traits=["CoP", "Fake"]
    ),
    "Sun Flower Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Sun",
        traits=["CoP", "Fake"]
    ),
    "Moon Flower Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Moon",
        traits=["CoP", "Fake"]
    ),
    "Forget Me Not Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Forget",
        traits=["CoP", "Fake"]
    ),
    "A Word of Thanks Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Thanks",
        traits=["CoP", "Fake"]
    ),
    "Fresh Fertilizer Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Fresh",
        traits=["CoP", "Fake"]
    ),
    "For the Future Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Future",
        traits=["CoP", "Fake"]
    ),
    "Echoes of a Drum Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Drum",
        traits=["CoP", "Fake"]
    ),
    "A Voice from Below Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Below",
        traits=["CoP", "Fake"]
    ),
    "Brain Over Brawn Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Brain",
        traits=["CoP", "Fake"]
    ),
    "Hunter's Challenge Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Hunter",
        traits=["CoP", "Fake"]
    ),
    "Moghan's Plea Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Plea",
        traits=["CoP", "Fake"]
    ),
    "Gatekeeper's Curiosity Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Gatekeeper",
        traits=["CoP", "Fake"]
    ),
    "Chocobo Chow Event (1)": LRFF13EventData(
        region="CoP Wildlands",
        item="C_Chow",
        traits=["CoP", "Fake"]
    ),
    "Secret Machine Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Secret",
        traits=["CoP", "Fake"]
    ),
    "Soulful Horn Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Soulful",
        traits=["CoP", "Fake"]
    ),
    "A Dangerous Cocktail Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Dangerous",
        traits=["CoP", "Fake"]
    ),
    "A Man for a Chocobo Girl Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Girl",
        traits=["CoP", "Fake"]
    ),
    "Source of Inspiration Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Inspiration",
        traits=["CoP", "Fake"]
    ),
    "True Colors Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Colors",
        traits=["CoP", "Fake"]
    ),
    "Youth Potion Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Youth",
        traits=["CoP", "Fake"]
    ),
    "Spell for Spell Event (1)": LRFF13EventData(
        region="CoP Yusnaan",
        item="C_Spell",
        traits=["CoP", "Fake"]
    ),
    "Dead Dunes Area Unlock Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="AreaUnlock",
        traits=["Fake"]
    ),
    "Wildlands Area Unlock Event (1)": LRFF13EventData(
        region="Wildlands",
        item="AreaUnlock",
        traits=["Fake"]
    ),
    "Yusnaan Area Unlock Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="AreaUnlock",
        traits=["Fake"]
    ),
    "Luxerion Area Unlock Event (1)": LRFF13EventData(
        region="Luxerion",
        item="AreaUnlock",
        traits=["Fake"]
    ),
    "Ultimate Lair Unlock Event (1)": LRFF13EventData(
        region="Ultimate Lair",
        item="ULUnlock",
        traits=["Fake"]
    ),
    "Tattered Leather Event (1)": LRFF13EventData(
        region="Shops",
        item="M_TatteredLeather",
        traits=["mat_z_000", "Fake"]
    ),
    "Vibrant Ooze Event (1)": LRFF13EventData(
        region="Shops",
        item="M_VibrantOoze",
        traits=["mat_z_001", "Fake"]
    ),
    "Niblet Hairball Event (1)": LRFF13EventData(
        region="Shops",
        item="M_NibletHairball",
        traits=["mat_z_002", "Fake"]
    ),
    "Slug Sweet Event (1)": LRFF13EventData(
        region="Shops",
        item="M_SlugSweet",
        traits=["mat_z_003", "Fake"]
    ),
    "Monster Mince Event (1)": LRFF13EventData(
        region="Shops",
        item="M_MonsterMince",
        traits=["mat_z_004", "Fake"]
    ),
    "Clear Ooze Event (1)": LRFF13EventData(
        region="Shops",
        item="M_ClearOoze",
        traits=["mat_z_007", "Fake"]
    ),
    "Green Leather Event (1)": LRFF13EventData(
        region="Shops",
        item="M_GreenLeather",
        traits=["mat_z_008", "Fake"]
    ),
    "Radial Bearing Event (1)": LRFF13EventData(
        region="Shops",
        item="M_RadialBearing",
        traits=["mat_z_009", "Fake"]
    ),
    "Goblot Hairball Event (1)": LRFF13EventData(
        region="Shops",
        item="M_GoblotHairball",
        traits=["mat_z_010", "Fake"]
    ),
    "Arboreal Spore Event (1)": LRFF13EventData(
        region="Shops",
        item="M_ArborealSpore",
        traits=["mat_z_011", "Fake"]
    ),
    "Dead Man's Teeth Event (1)": LRFF13EventData(
        region="Shops",
        item="M_DeadMansTeeth",
        traits=["mat_z_012", "Fake"]
    ),
    "Chipped Fang Event (1)": LRFF13EventData(
        region="Shops",
        item="M_ChippedFang",
        traits=["mat_z_013", "Fake"]
    ),
    "Shattered Bone Event (1)": LRFF13EventData(
        region="Shops",
        item="M_ShatteredBone",
        traits=["mat_z_014", "Fake"]
    ),
    "Goopy Goo Event (1)": LRFF13EventData(
        region="Shops",
        item="M_GoopyGoo",
        traits=["mat_z_015", "Fake"]
    ),
    "Pot Shard Event (1)": LRFF13EventData(
        region="Shops",
        item="M_PotShard",
        traits=["mat_z_016", "Fake"]
    ),
    "Dried Scale Event (1)": LRFF13EventData(
        region="Shops",
        item="M_DriedScale",
        traits=["mat_z_017", "Fake"]
    ),
    "Wonder Gel Event (1)": LRFF13EventData(
        region="Shops",
        item="M_WonderGel",
        traits=["mat_z_018", "Fake"]
    ),
    "Poisonous Sting Event (1)": LRFF13EventData(
        region="Shops",
        item="M_PoisonousSting",
        traits=["mat_z_019", "Fake"]
    ),
    "Motor Coil Event (1)": LRFF13EventData(
        region="Shops",
        item="M_MotorCoil",
        traits=["mat_z_020", "Fake"]
    ),
    "Ether Coil Event (1)": LRFF13EventData(
        region="Shops",
        item="M_EtherCoil",
        traits=["mat_z_021", "Fake"]
    ),
    "Demon Spicule Event (1)": LRFF13EventData(
        region="Shops",
        item="M_DemonSpicule",
        traits=["mat_z_022", "Fake"]
    ),
    "Organic Carapace Event (1)": LRFF13EventData(
        region="Shops",
        item="M_OrganicCarapace",
        traits=["mat_z_024", "Fake"]
    ),
    "Firewyrm Scale Event (1)": LRFF13EventData(
        region="Shops",
        item="M_FirewyrmScale",
        traits=["mat_z_028", "Fake"]
    ),
    "Quality Machine Oil Event (1)": LRFF13EventData(
        region="Shops",
        item="M_QualityMachineOil",
        traits=["mat_z_029", "Fake"]
    ),
    "Sinister Fang Event (1)": LRFF13EventData(
        region="Shops",
        item="M_SinisterFang",
        traits=["mat_z_030", "Fake"]
    ),
    "Stormdragon Down Event (1)": LRFF13EventData(
        region="Shops",
        item="M_StormdragonDown",
        traits=["mat_z_031", "Fake"]
    ),
    "Green Monster Moss Event (1)": LRFF13EventData(
        region="Shops",
        item="M_GreenMonsterMoss",
        traits=["mat_z_032", "Fake"]
    ),
    "Desert Rose Event (1)": LRFF13EventData(
        region="Shops",
        item="M_DesertRose",
        traits=["mat_z_033", "Fake"]
    ),
    "Single Eye Event (1)": LRFF13EventData(
        region="Shops",
        item="M_SingleEye",
        traits=["mat_z_035", "Fake"]
    ),
    "AMP Chip Event (1)": LRFF13EventData(
        region="Shops",
        item="M_AMPChip",
        traits=["mat_z_036", "Fake"]
    ),
    "Cactuar Doll Event (1)": LRFF13EventData(
        region="Shops",
        item="M_CactuarDoll",
        traits=["mat_z_044", "Fake"]
    ),
    "Liquid Glass Event (1)": LRFF13EventData(
        region="Shops",
        item="M_LiquidGlass",
        traits=["mat_z_045", "Fake"]
    ),
    "0-1 Hint Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="0-1 Hint",
        traits=["Fake"]
    ),
    "1-1 Hint Event (1)": LRFF13EventData(
        region="Luxerion",
        item="1-1 Hint",
        traits=["Fake"]
    ),
    "1-2 Hint Event (1)": LRFF13EventData(
        region="Luxerion",
        item="1-2 Hint",
        traits=["Fake"]
    ),
    "1-3 Hint Event (1)": LRFF13EventData(
        region="Luxerion",
        item="1-3 Hint",
        traits=["Fake"]
    ),
    "1-4 Hint Event (1)": LRFF13EventData(
        region="Luxerion",
        item="1-4 Hint",
        traits=["Fake"]
    ),
    "1-5 Hint Event (1)": LRFF13EventData(
        region="Luxerion",
        item="1-5 Hint",
        traits=["Fake"]
    ),
    "2-1 Hint Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="2-1 Hint",
        traits=["Fake"]
    ),
    "2-2 Hint Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="2-2 Hint",
        traits=["Fake"]
    ),
    "2-3 Hint Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="2-3 Hint",
        traits=["Fake"]
    ),
    "3-1 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="3-1 Hint",
        traits=["Fake"]
    ),
    "3-2 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="3-2 Hint",
        traits=["Fake"]
    ),
    "3-3 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="3-3 Hint",
        traits=["Fake"]
    ),
    "4-1 Hint Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="4-1 Hint",
        traits=["Fake"]
    ),
    "4-2 Hint Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="4-2 Hint",
        traits=["Fake"]
    ),
    "4-3 Hint Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="4-3 Hint",
        traits=["Fake"]
    ),
    "4-4 Hint Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="4-4 Hint",
        traits=["Fake"]
    ),
    "4-5 Hint Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="4-5 Hint",
        traits=["Fake"]
    ),
    "5-1 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="5-1 Hint",
        traits=["Fake"]
    ),
    "5-2 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="5-2 Hint",
        traits=["Fake"]
    ),
    "5-3 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="5-3 Hint",
        traits=["Fake"]
    ),
    "5-4 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="5-4 Hint",
        traits=["Fake"]
    ),
    "5-5 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="5-5 Hint",
        traits=["Fake"]
    ),
    "5-6 Hint Event (1)": LRFF13EventData(
        region="Wildlands",
        item="5-6 Hint",
        traits=["Fake"]
    ),
    "shop_itm_dd03_3 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd03_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd01_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd01_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd02_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd02_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd04_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd04_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx00_2 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx00_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx01_2 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx01_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx02_2 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx02_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl00_2 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl00_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl01_2 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl01_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl02_2 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl02_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl03_2 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl03_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys00_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys00_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys01_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys01_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys06_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys06_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys02_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys02_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys03_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys03_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys04_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys04_2_Shop",
        traits=["Fake"]
    ),
    "shop_ptl_pt00_2 Shop Event (1)": LRFF13EventData(
        region="Ark",
        item="shop_ptl_pt00_2_Shop",
        traits=["Fake"]
    ),
    "shop_cus_dd00_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_cus_dd00_2_Shop",
        traits=["Fake"]
    ),
    "shop_cus_lx00_2 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_cus_lx00_2_Shop",
        traits=["Fake"]
    ),
    "shop_cus_wl00_2 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_cus_wl00_2_Shop",
        traits=["Fake"]
    ),
    "shop_cus_wl01_2 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_cus_wl01_2_Shop",
        traits=["Fake"]
    ),
    "shop_cus_ys00_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_cus_ys00_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wd00_2 Shop Event (1)": LRFF13EventData(
        region="Anywhere",
        item="shop_equ_wd00_2_Shop",
        traits=["Fake"]
    ),
    "shop_cus_dd00 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_cus_dd00_Shop",
        traits=["Fake"]
    ),
    "shop_equ_dd00 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_equ_dd00_Shop",
        traits=["Fake"]
    ),
    "shop_equ_dd02 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_equ_dd02_Shop",
        traits=["Fake"]
    ),
    "shop_equ_lx00 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_equ_lx00_Shop",
        traits=["Fake"]
    ),
    "shop_equ_lx02 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_equ_lx02_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wl00 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_equ_wl00_Shop",
        traits=["Fake"]
    ),
    "shop_equ_ys00 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_equ_ys00_Shop",
        traits=["Fake"]
    ),
    "shop_equ_ys01 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_equ_ys01_Shop",
        traits=["Fake"]
    ),
    "shop_equ_ys02 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_equ_ys02_Shop",
        traits=["Fake"]
    ),
    "shop_cus_lx00 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_cus_lx00_Shop",
        traits=["Fake"]
    ),
    "shop_cus_wl00 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_cus_wl00_Shop",
        traits=["Fake"]
    ),
    "shop_cus_wl01 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_cus_wl01_Shop",
        traits=["Fake"]
    ),
    "shop_cus_ys00 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_cus_ys00_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wd00 Shop Event (1)": LRFF13EventData(
        region="Anywhere",
        item="shop_equ_wd00_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd00 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd00_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd03_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd03_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd01 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd01_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd02 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd02_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd04 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd04_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx00 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx00_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx01 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx01_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx02 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx02_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl00 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl00_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl01 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl01_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl02 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl02_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl03 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl03_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys00 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys00_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys01 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys01_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys06_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys06_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys02 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys02_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys03 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys03_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys04 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys04_Shop",
        traits=["Fake"]
    ),
    "shop_ptl_pt00 Shop Event (1)": LRFF13EventData(
        region="Ark",
        item="shop_ptl_pt00_Shop",
        traits=["Fake"]
    ),
    "shop_cus_dd00_3 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_cus_dd00_3_Shop",
        traits=["Fake"]
    ),
    "shop_cus_lx00_3 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_cus_lx00_3_Shop",
        traits=["Fake"]
    ),
    "shop_cus_lx50 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_cus_lx50_Shop",
        traits=["Fake"]
    ),
    "shop_cus_wl00_3 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_cus_wl00_3_Shop",
        traits=["Fake"]
    ),
    "shop_cus_wl01_3 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_cus_wl01_3_Shop",
        traits=["Fake"]
    ),
    "shop_cus_ys00_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_cus_ys00_3_Shop",
        traits=["Fake"]
    ),
    "shop_equ_dd00_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_equ_dd00_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_dd02_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_equ_dd02_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_lx00_2 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_equ_lx00_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_lx01 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_equ_lx01_Shop",
        traits=["Fake"]
    ),
    "shop_equ_lx02_2 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_equ_lx02_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_lx03_3 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_equ_lx03_3_Shop",
        traits=["Fake"]
    ),
    "shop_equ_lx50 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_equ_lx50_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wd00_3 Shop Event (1)": LRFF13EventData(
        region="Anywhere",
        item="shop_equ_wd00_3_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wl00_2 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_equ_wl00_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wl04_3 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_equ_wl04_3_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wl01 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_equ_wl01_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wl02 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_equ_wl02_Shop",
        traits=["Fake"]
    ),
    "shop_equ_wl03 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_equ_wl03_Shop",
        traits=["Fake"]
    ),
    "shop_equ_ys00_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_equ_ys00_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_ys03_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_equ_ys03_3_Shop",
        traits=["Fake"]
    ),
    "shop_equ_ys01_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_equ_ys01_2_Shop",
        traits=["Fake"]
    ),
    "shop_equ_ys02_2 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_equ_ys02_2_Shop",
        traits=["Fake"]
    ),
    "shop_etc_dd00 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_etc_dd00_Shop",
        traits=["Fake"]
    ),
    "shop_etc_lx00 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_etc_lx00_Shop",
        traits=["Fake"]
    ),
    "shop_etc_lx01 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_etc_lx01_Shop",
        traits=["Fake"]
    ),
    "shop_etc_wl00 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_etc_wl00_Shop",
        traits=["Fake"]
    ),
    "shop_etc_wl01 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_etc_wl01_Shop",
        traits=["Fake"]
    ),
    "shop_etc_wl02 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_etc_wl02_Shop",
        traits=["Fake"]
    ),
    "shop_etc_ys00 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_etc_ys00_Shop",
        traits=["Fake"]
    ),
    "shop_etc_ys01 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_etc_ys01_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd00_2 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd00_2_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd03_4 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd03_4_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd01_3 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd01_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd02_3 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd02_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_dd04_3 Shop Event (1)": LRFF13EventData(
        region="Dead Dunes",
        item="shop_itm_dd04_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx00_3 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx00_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx01_3 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx01_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx02_3 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx02_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx50 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx50_Shop",
        traits=["Fake"]
    ),
    "shop_itm_lx51 Shop Event (1)": LRFF13EventData(
        region="Luxerion",
        item="shop_itm_lx51_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl00_3 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl00_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl01_3 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl01_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl02_3 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl02_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_wl03_3 Shop Event (1)": LRFF13EventData(
        region="Wildlands",
        item="shop_itm_wl03_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys00_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys00_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys01_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys01_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys06_4 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys06_4_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys02_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys02_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys03_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys03_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys04_3 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys04_3_Shop",
        traits=["Fake"]
    ),
    "shop_itm_ys05 Shop Event (1)": LRFF13EventData(
        region="Yusnaan",
        item="shop_itm_ys05_Shop",
        traits=["Fake"]
    ),
    "shop_ptl_pt00_3 Shop Event (1)": LRFF13EventData(
        region="Ark",
        item="shop_ptl_pt00_3_Shop",
        traits=["Fake"]
    ),
    "shop_ptl_pt01 Shop Event (1)": LRFF13EventData(
        region="Ark",
        item="shop_ptl_pt01_Shop",
        traits=["Fake"]
    ),
}
