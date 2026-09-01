from typing import Dict, NamedTuple, Optional
from BaseClasses import Location, LocationProgressType


class LRFF13Location(Location):
    game: str = "Lightning Returns: Final Fantasy XIII"


class LRFF13LocationData(NamedTuple):
    region: str
    type: str
    str_id: str
    address: Optional[int] = None
    classification: LocationProgressType = LocationProgressType.DEFAULT
    original_item: str = None


location_data_table: Dict[str, LRFF13LocationData] = {
    "Dead Dunes - Golden Scarab Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=1,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_008",
        original_item="key_b_08"
    ),
    "Dead Dunes - Oasis Lighthouse Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=2,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_009",
        original_item="key_b_09"
    ),
    "Dead Dunes - Grave of the Colossi Shrine Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=3,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_011",
        original_item="key_b_11"
    ),
    "Dead Dunes - Giant's Sandbox Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=4,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_001",
        original_item="libra_m370"
    ),
    "Dead Dunes - Golden Chamber Lower Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=5,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_002",
        original_item="acc_a_4100"
    ),
    "Dead Dunes - Giant's Sandbox Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=6,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_003",
        original_item="acc_b_4130"
    ),
    "Dead Dunes - Giant's Sandbox Treasure (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=7,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_004",
        original_item="at010_50_10"
    ),
    "Dead Dunes - Giant's Sandbox Treasure (4)": LRFF13LocationData(
        region="Dead Dunes",
        address=8,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_005",
        original_item="mg570_00_10"
    ),
    "Dead Dunes - Ruffian Outdoor Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=9,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_006",
        original_item="acc_a_3010"
    ),
    "Dead Dunes - Dry Floodlands Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=10,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_007",
        original_item="acc_b_4160"
    ),
    "Dead Dunes - Oasis Lighthouse Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=11,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_008",
        original_item="acc_a_8120"
    ),
    "Dead Dunes - Oasis Lighthouse Treasure (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=12,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_009",
        original_item="acc_a_5100"
    ),
    "Dead Dunes - Atomos's Sand Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=13,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_010",
        original_item="acc_a_1040"
    ),
    "Dead Dunes - Grave of the Colossi Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=14,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_011",
        original_item="acc_b_4140"
    ),
    "Dead Dunes - Grave of the Colossi Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=15,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_012",
        original_item="acc_a_5200"
    ),
    "Dead Dunes - Grave of the Colossi Treasure (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=16,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_013",
        original_item="libra_m355"
    ),
    "Dead Dunes - Atomos's Sand Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=17,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_014",
        original_item="acc_b_4210"
    ),
    "Dead Dunes - Ruffian 2nd Floor Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=18,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_015",
        original_item="libra_m406"
    ),
    "Dead Dunes - Temple Ruins Chamber of Dusk (Upper) Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=19,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_016",
        original_item="acc_a_1030"
    ),
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Upper) Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=20,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_017",
        original_item="acc_b_4170"
    ),
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Upper) Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=21,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_018",
        original_item="mg500_00_10"
    ),
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Upper) Treasure (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=22,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_019",
        original_item="mg000_00_10"
    ),
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Lower) Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=23,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_020",
        original_item="acc_b_4200"
    ),
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Lower) Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=24,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_021",
        original_item="acc_b_4180"
    ),
    "Dead Dunes - Temple Ruins Chamber of Plenilune (Lower) Treasure (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=25,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_022",
        original_item="mg010_00_10"
    ),
    "Dead Dunes - Temple Ruins Sacred Grove Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=26,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_023",
        original_item="libra_m770"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=27,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_024",
        original_item="acc_b_7020"
    ),
    "Dead Dunes - Dry Floodlands Shrine Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=28,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_025",
        original_item="acc_b_4190"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=29,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_026",
        original_item="acc_b_6220"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=30,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_027",
        original_item="acc_a_8130"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Treasure (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=31,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_028",
        original_item="mg020_00_10"
    ),
    "Dead Dunes - Temple Ruins Scorched Earth (Lower) Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=32,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_029",
        original_item="acc_b_7200"
    ),
    "Dead Dunes - Temple Ruins Scorched Earth (Upper) Treasure (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=33,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_030",
        original_item="acc_a_8010"
    ),
    "Dead Dunes - Temple Ruins Scorched Earth (Upper) Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=34,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_031",
        original_item="acc_a_8400"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=35,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_032",
        original_item="acc_b_7100"
    ),
    "Dead Dunes - Atomos's Sands Shrine Treasure": LRFF13LocationData(
        region="Dead Dunes",
        address=36,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_033",
        original_item="acc_b_4150"
    ),
    "Dead Dunes - Giant's Sandbox Treasure (5)": LRFF13LocationData(
        region="Dead Dunes",
        address=37,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_034",
        original_item="mg560_00_10"
    ),
    "Dead Dunes - Dry Floodlands Treasure (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=38,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_d_035",
        original_item="libra_m253_afr"
    ),
    "Dead Dunes - Grave of the Colossi Shrine Tablet": LRFF13LocationData(
        region="Dead Dunes",
        address=39,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_seki_1",
        original_item="key_d_sekiban"
    ),
    "Dead Dunes - Dry Floodlands Shrine Tablet": LRFF13LocationData(
        region="Dead Dunes",
        address=40,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_seki_2",
        original_item="key_d_sekiban"
    ),
    "Dead Dunes - Atomos's Sands Shrine Tablet": LRFF13LocationData(
        region="Dead Dunes",
        address=41,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_seki_3",
        original_item="key_d_sekiban"
    ),
    "Dead Dunes - Temple Ruins Mural Crux Base": LRFF13LocationData(
        region="Dead Dunes",
        address=42,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_base",
        original_item="key_d_base"
    ),
    "Dead Dunes - Temple Ruins Mural Crux Body": LRFF13LocationData(
        region="Dead Dunes",
        address=43,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_wing",
        original_item="key_d_wing"
    ),
    "Dead Dunes - Temple Ruins Mural Crux Tip": LRFF13LocationData(
        region="Dead Dunes",
        address=44,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_top",
        original_item="key_d_top"
    ),
    "Dead Dunes - Ruffian Shop Bhakti's Oil Spot": LRFF13LocationData(
        region="Dead Dunes",
        address=45,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_oil1",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Oasis Lighthouse Bhakti's Oil Spot (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=46,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_oil2",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Oasis Lighthouse Bhakti's Oil Spot (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=47,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_oil3",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Oasis Lighthouse Bhakti's Oil Spot (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=48,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_oil4",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Atomos's Sands Shrine Bhakti's Oil Spot": LRFF13LocationData(
        region="Dead Dunes",
        address=49,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_oil5",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Grave of the Colossi Bones Bhakti's Oil Spot": LRFF13LocationData(
        region="Dead Dunes",
        address=50,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_oil6",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Dry Floodlands Shrine Bhakti's Oil Spot": LRFF13LocationData(
        region="Dead Dunes",
        address=51,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_oil7",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Temple Ruins Bhakti Reward (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=52,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_d_bakt"
    ),
    "Dead Dunes - Temple Ruins Bhakti Reward (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=53,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_bakt_oil",
        original_item="key_d_oil"
    ),
    "Dead Dunes - Temple Ruins Bhakti Reward (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=54,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_d_bakt_key",
        original_item="key_d_key"
    ),
    "Dead Dunes - Grave of the Colossi Pilgrim's Crux": LRFF13LocationData(
        region="Dead Dunes",
        address=55,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye1",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Scorched Earth Pilgrim's Crux (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=56,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye10",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=57,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye11",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Scorched Earth Pilgrim's Crux (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=58,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye12",
        original_item="key_d_key"
    ),
    "Dead Dunes - Dry Floodlands Pilgrim's Crux": LRFF13LocationData(
        region="Dead Dunes",
        address=59,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye13",
        original_item="key_d_key"
    ),
    "Dead Dunes - Atomos's Sands Pilgrim's Crux": LRFF13LocationData(
        region="Dead Dunes",
        address=60,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye14",
        original_item="key_d_key"
    ),
    "Dead Dunes - Giant's Sandbox Pilgrim's Crux": LRFF13LocationData(
        region="Dead Dunes",
        address=61,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye2",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=62,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye3",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=63,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye4",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=64,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye5",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=65,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye6",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Upper) Pilgrim's Crux (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=66,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye7",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Sacred Grove Pilgrim's Crux (4)": LRFF13LocationData(
        region="Dead Dunes",
        address=67,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye8",
        original_item="key_d_key"
    ),
    "Dead Dunes - Temple Ruins Golden Chamber (Lower) Pilgrim's Crux (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=68,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_dkye9",
        original_item="key_d_key"
    ),
    "Dead Dunes - Atomos's Sands Loupe": LRFF13LocationData(
        region="Dead Dunes",
        address=69,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_lupe",
        original_item="key_d_lupe"
    ),
    "Dead Dunes - The Life of a Machine Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=70,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_041"
    ),
    "Dead Dunes - The Life of a Machine Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=71,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_041_2",
        original_item="e524"
    ),
    "Dead Dunes - Old Rivals Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=72,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_042"
    ),
    "Dead Dunes - Old Rivals Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=73,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_042_2",
        original_item="e540"
    ),
    "Dead Dunes - His Wife's Dream Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=74,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_044"
    ),
    "Dead Dunes - His Wife's Dream Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=75,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_044_2",
        original_item="e340"
    ),
    "Dead Dunes - Tool of the Trade Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=76,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_045"
    ),
    "Dead Dunes - Tool of the Trade Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=77,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_045_2",
        original_item="e519"
    ),
    "Dead Dunes - Adonis's Audition Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=78,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_046"
    ),
    "Dead Dunes - Adonis's Audition Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=79,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_046_2",
        original_item="e525"
    ),
    "Dead Dunes - Adonis's Audition Quest (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=80,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_046_3",
        original_item="key_r_rec"
    ),
    "Dead Dunes - What Rough Beast Slouches Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=81,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_047"
    ),
    "Dead Dunes - What Rough Beast Slouches Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=82,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_047_2",
        original_item="e549"
    ),
    "Dead Dunes - Skeletons In The Closet Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=83,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_048"
    ),
    "Dead Dunes - Skeletons In The Closet Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=84,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_048_2",
        original_item="e530"
    ),
    "Dead Dunes - Last One Standing Quest (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=85,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_049"
    ),
    "Dead Dunes - Last One Standing Quest (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=86,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_049_2",
        original_item="wea_oa17"
    ),
    "Dead Dunes - Last One Standing Quest (3)": LRFF13LocationData(
        region="Dead Dunes",
        address=87,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_049_3",
        original_item="e557"
    ),
    "Dead Dunes - What Rough Beast Slouches Libra Notes": LRFF13LocationData(
        region="Dead Dunes",
        address=88,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_libra_m375",
        original_item="libra_m375"
    ),
    "Dead Dunes - Dead Dunes Boss Drop": LRFF13LocationData(
        region="Dead Dunes",
        address=89,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9060",
        original_item="acc_a_9060"
    ),
    "Dead Dunes - Dead Dunes Boss Reward (1)": LRFF13LocationData(
        region="Dead Dunes",
        address=90,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9020",
        original_item="key_r_atb"
    ),
    "Dead Dunes - Dead Dunes Boss Reward (2)": LRFF13LocationData(
        region="Dead Dunes",
        address=91,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9020_2",
        original_item="key_r_rec"
    ),
    "Dead Dunes - Aeronite Missable Drop": LRFF13LocationData(
        region="Dead Dunes",
        address=92,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_acc_a_9200",
        original_item="acc_a_9200"
    ),
    "Luxerion - Cathedral Proof Of Courage": LRFF13LocationData(
        region="Luxerion",
        address=93,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_000",
        original_item="key_b_00"
    ),
    "Luxerion - Pilgrim's Passage Violet Amulet Treasure": LRFF13LocationData(
        region="Luxerion",
        address=94,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_001",
        original_item="key_b_01"
    ),
    "Luxerion - North Station Plaza Treasure": LRFF13LocationData(
        region="Luxerion",
        address=95,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_000",
        original_item="acc_a_0000"
    ),
    "Luxerion - The Avenue Treasure": LRFF13LocationData(
        region="Luxerion",
        address=96,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_001",
        original_item="acc_a_3000"
    ),
    "Luxerion - Gallery Steps Treasure": LRFF13LocationData(
        region="Luxerion",
        address=97,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_002",
        original_item="acc_a_0010"
    ),
    "Luxerion - 2nd Ave Treasure": LRFF13LocationData(
        region="Luxerion",
        address=98,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_003",
        original_item="gd020_00_10"
    ),
    "Luxerion - Pilgrim's Passage (Grassy) Treasure": LRFF13LocationData(
        region="Luxerion",
        address=99,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_004",
        original_item="acc_b_1000"
    ),
    "Luxerion - Old Theater Platform Treasure": LRFF13LocationData(
        region="Luxerion",
        address=100,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_005",
        original_item="acc_b_1010"
    ),
    "Luxerion - The Warren Mangled Hill Treasure": LRFF13LocationData(
        region="Luxerion",
        address=101,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_006",
        original_item="mb210_00_10"
    ),
    "Luxerion - South Station (Supply Sphere) Treasure": LRFF13LocationData(
        region="Luxerion",
        address=102,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_009",
        original_item="libra_m293"
    ),
    "Luxerion - Warehouse District (Supply Sphere) Treasure": LRFF13LocationData(
        region="Luxerion",
        address=103,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_010",
        original_item="libra_m291"
    ),
    "Luxerion - Residences (Supply Sphere) Treasure": LRFF13LocationData(
        region="Luxerion",
        address=104,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_011",
        original_item="libra_m380"
    ),
    "Luxerion - Forsaken Graveyard Treasure (1)": LRFF13LocationData(
        region="Luxerion",
        address=105,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_012",
        original_item="acc_a_1130"
    ),
    "Luxerion - Den Of Shadows Treasure (1)": LRFF13LocationData(
        region="Luxerion",
        address=106,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_013",
        original_item="acc_b_6100"
    ),
    "Luxerion - Luxerion After 1st Phone (1)": LRFF13LocationData(
        region="Luxerion",
        address=107,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_014",
        original_item="gil_l_000"
    ),
    "Luxerion - Den Of Shadows Treasure (2)": LRFF13LocationData(
        region="Luxerion",
        address=108,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_015",
        original_item="wea_oa15"
    ),
    "Luxerion - Luxerion After 1st Phone (2)": LRFF13LocationData(
        region="Luxerion",
        address=109,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_016",
        original_item="gil_l_000"
    ),
    "Luxerion - Luxerion After 1st Phone (3)": LRFF13LocationData(
        region="Luxerion",
        address=110,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_017",
        original_item="gil_l_010"
    ),
    "Luxerion - Luxerion Marketplace Treasure": LRFF13LocationData(
        region="Luxerion",
        address=111,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_019",
        original_item="at010_30_10"
    ),
    "Luxerion - Forsaken Graveyard Treasure (2)": LRFF13LocationData(
        region="Luxerion",
        address=112,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_l_020",
        original_item="acc_a_5000"
    ),
    "Luxerion - 1st Ave Rubber Ball": LRFF13LocationData(
        region="Luxerion",
        address=113,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_ball",
        original_item="key_ball"
    ),
    "Luxerion - Marketplace Doll": LRFF13LocationData(
        region="Luxerion",
        address=114,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_kb_g",
        original_item="key_kb_g"
    ),
    "Luxerion - North Station Plaza Doll": LRFF13LocationData(
        region="Luxerion",
        address=115,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_kb_r",
        original_item="key_kb_r"
    ),
    "Luxerion - Warehouse District Thunderclap Cap": LRFF13LocationData(
        region="Luxerion",
        address=116,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_kino",
        original_item="key_j_kino"
    ),
    "Luxerion - Luxerion Proof of Legendary Title": LRFF13LocationData(
        region="Luxerion",
        address=117,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_kish",
        original_item="key_l_kishin"
    ),
    "Luxerion - Luxerion Ghost Phantom Rose": LRFF13LocationData(
        region="Luxerion",
        address=118,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_hana",
        original_item="key_l_hana"
    ),
    "Luxerion - Luxerion Marketplace Pen": LRFF13LocationData(
        region="Luxerion",
        address=119,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_pen",
        original_item="key_l_pen"
    ),
    "Luxerion - Baird Seedhunter Membership Card": LRFF13LocationData(
        region="Luxerion",
        address=120,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="trd_soulcd",
        original_item="key_soulcd"
    ),
    "Luxerion - Virgil Supply Sphere Password": LRFF13LocationData(
        region="Luxerion",
        address=121,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_kyu_pass",
        original_item="key_kyu_pass"
    ),
    "Luxerion - Buy Shaolong Gui Shell": LRFF13LocationData(
        region="Luxerion",
        address=122,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="trd_niku",
        original_item="key_niku"
    ),
    "Luxerion - Buy Mandragora Root": LRFF13LocationData(
        region="Luxerion",
        address=123,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="trd_ninjin",
        original_item="key_ninjin"
    ),
    "Luxerion - Chocobo Emporium Spectral Elixir": LRFF13LocationData(
        region="Luxerion",
        address=124,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_bt_sp",
        original_item="key_sp_bt"
    ),
    "Luxerion - The Things She Lost Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=125,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_001"
    ),
    "Luxerion - The Things She Lost Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=126,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_001_2",
        original_item="e092"
    ),
    "Luxerion - Where Are You, Holmes? Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=127,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_002"
    ),
    "Luxerion - Where Are You, Holmes? Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=128,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_002_2",
        original_item="e030"
    ),
    "Luxerion - Where Are You, Holmes? Quest (3)": LRFF13LocationData(
        region="Luxerion",
        address=129,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_002_3",
        original_item="e031"
    ),
    "Luxerion - Like Clockwork Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=130,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_003"
    ),
    "Luxerion - Like Clockwork Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=131,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_003_2",
        original_item="e212"
    ),
    "Luxerion - Dying Wish Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=132,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_004"
    ),
    "Luxerion - Dying Wish Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=133,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_004_2",
        original_item="e041"
    ),
    "Luxerion - Suspicious Spheres Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=134,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_005"
    ),
    "Luxerion - Suspicious Spheres Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=135,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_005_2",
        original_item="e703"
    ),
    "Luxerion - Born From Chaos Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=136,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_q006"
    ),
    "Luxerion - Born From Chaos Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=137,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_006"
    ),
    "Luxerion - Born From Chaos Quest (3)": LRFF13LocationData(
        region="Luxerion",
        address=138,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_006_2",
        original_item="shi_ba01"
    ),
    "Luxerion - Born From Chaos Quest (4)": LRFF13LocationData(
        region="Luxerion",
        address=139,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_006_3",
        original_item="e552"
    ),
    "Luxerion - Soul Seeds Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=140,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_007"
    ),
    "Luxerion - Soul Seeds Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=141,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_007_2",
        original_item="e255"
    ),
    "Luxerion - Faster Than Lightning Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=142,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_008"
    ),
    "Luxerion - Faster Than Lightning Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=143,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_008_2",
        original_item="e336"
    ),
    "Luxerion - Treasured Ball Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=144,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_009"
    ),
    "Luxerion - Treasured Ball Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=145,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_009_2",
        original_item="e269"
    ),
    "Luxerion - Talbot's Gratitude": LRFF13LocationData(
        region="Luxerion",
        address=146,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_kimo",
        original_item="key_kimochi"
    ),
    "Luxerion - The Angel's Tears Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=147,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_010"
    ),
    "Luxerion - The Angel's Tears Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=148,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_010_2",
        original_item="e047"
    ),
    "Luxerion - The Saint's Stone Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=149,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_011"
    ),
    "Luxerion - The Saint's Stone Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=150,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_011_2",
        original_item="cos_ha01"
    ),
    "Luxerion - The Saint's Stone Quest (3)": LRFF13LocationData(
        region="Luxerion",
        address=151,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_011_3",
        original_item="e083"
    ),
    "Luxerion - Aremiah Service Entrance Key": LRFF13LocationData(
        region="Luxerion",
        address=152,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_l_kagi",
        original_item="key_l_kagi"
    ),
    "Luxerion - Whither Faith Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=153,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_012"
    ),
    "Luxerion - Whither Faith Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=154,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_012_2",
        original_item="e513"
    ),
    "Luxerion - The Avid Reader Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=155,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_013"
    ),
    "Luxerion - The Avid Reader Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=156,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_013_2",
        original_item="e079"
    ),
    "Luxerion - Buried Passion Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=157,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_014"
    ),
    "Luxerion - Buried Passion Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=158,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_014_2",
        original_item="e321"
    ),
    "Luxerion - The Girl Who Cried Wolf Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=159,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_015"
    ),
    "Luxerion - The Girl Who Cried Wolf Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=160,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_015_2",
        original_item="e261"
    ),
    "Luxerion - Stuck in a Gem Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=161,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_016"
    ),
    "Luxerion - Stuck in a Gem Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=162,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_016_2",
        original_item="e572"
    ),
    "Luxerion - Get the Girl Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=163,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_017"
    ),
    "Luxerion - Get the Girl Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=164,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_017_2",
        original_item="e512"
    ),
    "Luxerion - A Rose By Any Other Name Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=165,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_019"
    ),
    "Luxerion - A Rose By Any Other Name Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=166,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_019_2",
        original_item="cos_ja02"
    ),
    "Luxerion - A Rose By Any Other Name Quest (3)": LRFF13LocationData(
        region="Luxerion",
        address=167,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_019_3",
        original_item="e046"
    ),
    "Luxerion - A Rose By Any Other Name Quest (4)": LRFF13LocationData(
        region="Luxerion",
        address=168,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_019_4",
        original_item="e320"
    ),
    "Luxerion - Voices from the Grave Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=169,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_020"
    ),
    "Luxerion - Voices from the Grave Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=170,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_020_2",
        original_item="e015"
    ),
    "Luxerion - To Save the Sinless Quest (1)": LRFF13LocationData(
        region="Luxerion",
        address=171,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_091"
    ),
    "Luxerion - To Save the Sinless Quest (2)": LRFF13LocationData(
        region="Luxerion",
        address=172,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_091_2",
        original_item="cos_ka01"
    ),
    "Luxerion - Replace Chronostasis": LRFF13LocationData(
        region="Luxerion",
        address=173,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_ti840",
        original_item="ti840_00"
    ),
    "Luxerion - Luxerion Boss Drop": LRFF13LocationData(
        region="Luxerion",
        address=174,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_wea_oa00",
        original_item="wea_oa00"
    ),
    "Luxerion - Luxerion Boss+ Only Missable Drop": LRFF13LocationData(
        region="Luxerion",
        address=175,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_wea_oa01",
        original_item="wea_oa01"
    ),
    "Luxerion - Luxerion Boss Reward (1)": LRFF13LocationData(
        region="Luxerion",
        address=176,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9000",
        original_item="key_r_ep"
    ),
    "Luxerion - Luxerion Boss Reward (2)": LRFF13LocationData(
        region="Luxerion",
        address=177,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9000_2",
        original_item="key_r_atb"
    ),
    "Wildlands - Moogle Village Moogle Dust Treasure": LRFF13LocationData(
        region="Wildlands",
        address=178,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_004",
        original_item="key_b_04"
    ),
    "Wildlands - Research Camp Photo Frame Treasure": LRFF13LocationData(
        region="Wildlands",
        address=179,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_005",
        original_item="key_b_05"
    ),
    "Wildlands - Poltae Etro's Forbidden Tome": LRFF13LocationData(
        region="Wildlands",
        address=180,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_006",
        original_item="key_b_06"
    ),
    "Wildlands - Eremite Plains Broken Gyroscope Treasure": LRFF13LocationData(
        region="Wildlands",
        address=181,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_007",
        original_item="key_b_07"
    ),
    "Wildlands - Aryas Village Treasure (1)": LRFF13LocationData(
        region="Wildlands",
        address=182,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_010",
        original_item="key_b_10"
    ),
    "Wildlands - Jagd Woods Treasure": LRFF13LocationData(
        region="Wildlands",
        address=183,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_000",
        original_item="acc_a_1120"
    ),
    "Wildlands - The Grasslands Treasure (1)": LRFF13LocationData(
        region="Wildlands",
        address=184,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_001",
        original_item="acc_b_6030"
    ),
    "Wildlands - Poltae Treasure (1)": LRFF13LocationData(
        region="Wildlands",
        address=185,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_002",
        original_item="acc_b_7110"
    ),
    "Wildlands - Canopus Farms Treasure": LRFF13LocationData(
        region="Wildlands",
        address=186,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_003",
        original_item="acc_a_0040"
    ),
    "Wildlands - Rocky Crag Treasure (1)": LRFF13LocationData(
        region="Wildlands",
        address=187,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_004",
        original_item="acc_a_1010"
    ),
    "Wildlands - The Grasslands Treasure (2)": LRFF13LocationData(
        region="Wildlands",
        address=188,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_005",
        original_item="acc_a_8210"
    ),
    "Wildlands - Aryas Village Treasure (2)": LRFF13LocationData(
        region="Wildlands",
        address=189,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_006",
        original_item="mb010_00_10"
    ),
    "Wildlands - The Grasslands Treasure (3)": LRFF13LocationData(
        region="Wildlands",
        address=190,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_007",
        original_item="acc_b_6050"
    ),
    "Wildlands - Eremite Plains Treasure (1)": LRFF13LocationData(
        region="Wildlands",
        address=191,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_008",
        original_item="acc_b_6040"
    ),
    "Wildlands - Eremite Plains Treasure (2)": LRFF13LocationData(
        region="Wildlands",
        address=192,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_009",
        original_item="mb110_00_10"
    ),
    "Wildlands - Moogle Village Treasure": LRFF13LocationData(
        region="Wildlands",
        address=193,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_010",
        original_item="acc_b_7010"
    ),
    "Wildlands - City of Ruins Treasure": LRFF13LocationData(
        region="Wildlands",
        address=194,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_011",
        original_item="acc_a_8300"
    ),
    "Wildlands - Rocky Crag Treasure (2)": LRFF13LocationData(
        region="Wildlands",
        address=195,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_012",
        original_item="acc_b_6060"
    ),
    "Wildlands - Rocky Crag Treasure (3)": LRFF13LocationData(
        region="Wildlands",
        address=196,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_013",
        original_item="acc_b_6110"
    ),
    "Wildlands - Aryas Village Treasure (3)": LRFF13LocationData(
        region="Wildlands",
        address=197,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_014",
        original_item="acc_a_1100"
    ),
    "Wildlands - Poltae Treasure (2)": LRFF13LocationData(
        region="Wildlands",
        address=198,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_015",
        original_item="mb410_00_10"
    ),
    "Wildlands - Eremite Plains Crash Site Fragment": LRFF13LocationData(
        region="Wildlands",
        address=199,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_016",
        original_item="key_s_kairaku"
    ),
    "Wildlands - Goddess Temple Treasure (1)": LRFF13LocationData(
        region="Wildlands",
        address=200,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_050",
        original_item="mc910_00_10"
    ),
    "Wildlands - Goddess Temple Treasure (2)": LRFF13LocationData(
        region="Wildlands",
        address=201,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_051",
        original_item="mb220_00_10"
    ),
    "Wildlands - Goddess Temple Treasure (3)": LRFF13LocationData(
        region="Wildlands",
        address=202,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_052",
        original_item="mb120_00_10"
    ),
    "Wildlands - Goddess Temple Treasure (4)": LRFF13LocationData(
        region="Wildlands",
        address=203,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_053",
        original_item="ma020_00_10"
    ),
    "Wildlands - Goddess Temple Treasure (5)": LRFF13LocationData(
        region="Wildlands",
        address=204,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_054",
        original_item="mb020_00_10"
    ),
    "Wildlands - Goddess Temple Treasure (6)": LRFF13LocationData(
        region="Wildlands",
        address=205,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_056",
        original_item="mb420_00_10"
    ),
    "Wildlands - Goddess Temple Treasure (7)": LRFF13LocationData(
        region="Wildlands",
        address=206,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_057",
        original_item="mc900_00_10"
    ),
    "Wildlands - Goddess Temple Treasure (8)": LRFF13LocationData(
        region="Wildlands",
        address=207,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_058",
        original_item="libra_m745"
    ),
    "Wildlands - Goddess Temple Treasure (9)": LRFF13LocationData(
        region="Wildlands",
        address=208,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_w_060",
        original_item="acc_a_1140"
    ),
    "Wildlands - Dr Gysahl's Gysahl Greens": LRFF13LocationData(
        region="Wildlands",
        address=209,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_yasai_t",
        original_item="key_w_yasai_t"
    ),
    "Wildlands - Aryas Village Beloved's Gift Treasure": LRFF13LocationData(
        region="Wildlands",
        address=210,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_s_okuri",
        original_item="key_s_okuri"
    ),
    "Wildlands - Sarala Vegatable Seeds": LRFF13LocationData(
        region="Wildlands",
        address=211,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_tane",
        original_item="key_w_tane"
    ),
    "Wildlands - A Father's Request Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=212,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_021"
    ),
    "Wildlands - A Father's Request Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=213,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_021_2",
        original_item="e516"
    ),
    "Wildlands - The Hunter's Challenge Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=214,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_022"
    ),
    "Wildlands - The Hunter's Challenge Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=215,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_022_2",
        original_item="cos_ea06"
    ),
    "Wildlands - The Hunter's Challenge Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=216,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_022_3",
        original_item="e343"
    ),
    "Wildlands - A Final Cure Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=217,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_023"
    ),
    "Wildlands - A Final Cure Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=218,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_023_2",
        original_item="e205"
    ),
    "Wildlands - A Final Cure Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=219,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_023_3",
        original_item="e206"
    ),
    "Wildlands - Fuzzy Search Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=220,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_024"
    ),
    "Wildlands - Fuzzy Search Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=221,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_024_2",
        original_item="e097"
    ),
    "Wildlands - Fuzzy Search Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=222,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_024_3",
        original_item="e068"
    ),
    "Wildlands - Round 'em Up Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=223,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_025"
    ),
    "Wildlands - Round 'em Up Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=224,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_025_2",
        original_item="e538"
    ),
    "Wildlands - Chocobo Cheer Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=225,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_026"
    ),
    "Wildlands - Chocobo Cheer Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=226,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_026_2",
        original_item="e301"
    ),
    "Wildlands - Chocobo Cheer Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=227,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_026_3",
        original_item="e338"
    ),
    "Wildlands - Peace and Quiet, Kupo Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=228,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_027"
    ),
    "Wildlands - Peace and Quiet, Kupo Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=229,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_027_2",
        original_item="key_w_mogsoul"
    ),
    "Wildlands - Peace and Quiet, Kupo Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=230,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_027_3",
        original_item="e093"
    ),
    "Wildlands - Peace and Quiet, Kupo Quest (4)": LRFF13LocationData(
        region="Wildlands",
        address=231,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_027_4",
        original_item="key_r_rec"
    ),
    "Wildlands - Saving an Angel Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=232,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_028"
    ),
    "Wildlands - Saving an Angel Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=233,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_028_2",
        original_item="e281"
    ),
    "Wildlands - Saving an Angel Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=234,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_028_3",
        original_item="key_r_rec"
    ),
    "Wildlands - Omega Point Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=235,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_029"
    ),
    "Wildlands - Omega Point Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=236,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_029_2",
        original_item="e265"
    ),
    "Wildlands - The Old Man and the Field Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=237,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_030"
    ),
    "Wildlands - The Old Man and the Field Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=238,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_030_2",
        original_item="e241"
    ),
    "Wildlands - Land of our Forebears Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=239,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_031"
    ),
    "Wildlands - Land of our Forebears Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=240,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_031_2",
        original_item="e242"
    ),
    "Wildlands - A Taste of the Past Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=241,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_032"
    ),
    "Wildlands - A Taste of the Past Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=242,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_032_2",
        original_item="e043"
    ),
    "Wildlands - A Taste of the Past Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=243,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_032_3",
        original_item="e051"
    ),
    "Wildlands - Dog, Doctor and Assistant Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=244,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_033"
    ),
    "Wildlands - Dog, Doctor and Assistant Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=245,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_033_2",
        original_item="e228"
    ),
    "Wildlands - Main Quest 5 (1)": LRFF13LocationData(
        region="Wildlands",
        address=246,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_034"
    ),
    "Wildlands - Main Quest 5 (2)": LRFF13LocationData(
        region="Wildlands",
        address=247,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_034_2",
        original_item="e339"
    ),
    "Wildlands - Main Quest 5 (3)": LRFF13LocationData(
        region="Wildlands",
        address=248,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_034_3",
        original_item="e070"
    ),
    "Wildlands - Main Quest 5 (4)": LRFF13LocationData(
        region="Wildlands",
        address=249,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_034_4",
        original_item="key_r_ep"
    ),
    "Wildlands - Main Quest 5 (5)": LRFF13LocationData(
        region="Wildlands",
        address=250,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_034_5",
        original_item="key_r_rec"
    ),
    "Wildlands - The Right Stuff Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=251,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_035"
    ),
    "Wildlands - The Right Stuff Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=252,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_035_2",
        original_item="e330"
    ),
    "Wildlands - The Secret Lives of Sheep Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=253,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_036"
    ),
    "Wildlands - The Secret Lives of Sheep Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=254,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_036_2",
        original_item="e517"
    ),
    "Wildlands - Where Are You, Moogle? Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=255,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_037"
    ),
    "Wildlands - Where Are You, Moogle? Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=256,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_037_2",
        original_item="e110"
    ),
    "Wildlands - Where Are You, Moogle? Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=257,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_037_3",
        original_item="e113"
    ),
    "Wildlands - Mercy of a Goddess Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=258,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_038"
    ),
    "Wildlands - Mercy of a Goddess Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=259,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_038_2",
        original_item="e304"
    ),
    "Wildlands - The Grail of Valhalla Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=260,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_039"
    ),
    "Wildlands - The Grail of Valhalla Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=261,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_039_2",
        original_item="cos_ka03"
    ),
    "Wildlands - The Grail of Valhalla Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=262,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_039_3",
        original_item="e062"
    ),
    "Wildlands - To Live in Chaos Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=263,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_040"
    ),
    "Wildlands - To Live in Chaos Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=264,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_040_2",
        original_item="wea_oa16"
    ),
    "Wildlands - To Live in Chaos Quest (3)": LRFF13LocationData(
        region="Wildlands",
        address=265,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_040_3",
        original_item="e012"
    ),
    "Wildlands - Killing Time Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=266,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_081"
    ),
    "Wildlands - Killing Time Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=267,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_081_2",
        original_item="e216"
    ),
    "Wildlands - Matchmaker Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=268,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_082"
    ),
    "Wildlands - Matchmaker Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=269,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_082_2",
        original_item="e307"
    ),
    "Wildlands - Mother and Daughter Quest (1)": LRFF13LocationData(
        region="Wildlands",
        address=270,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_083"
    ),
    "Wildlands - Mother and Daughter Quest (2)": LRFF13LocationData(
        region="Wildlands",
        address=271,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_083_2",
        original_item="e595"
    ),
    "Wildlands - The Secret Lives of Sheep Mystery Egg": LRFF13LocationData(
        region="Wildlands",
        address=272,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_tamago",
        original_item="key_w_tamago"
    ),
    "Wildlands - Goddess Temple Goddess Glyphs": LRFF13LocationData(
        region="Wildlands",
        address=273,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_moji1",
        original_item="key_w_moji1"
    ),
    "Wildlands - Goddess Temple Chaos Glyphs": LRFF13LocationData(
        region="Wildlands",
        address=274,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_moji2",
        original_item="key_w_moji2"
    ),
    "Wildlands - Poltae Plate Metal Fragment": LRFF13LocationData(
        region="Wildlands",
        address=275,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_buhin1",
        original_item="key_w_buhin1"
    ),
    "Wildlands - Poltae Silvered Metal Fragment": LRFF13LocationData(
        region="Wildlands",
        address=276,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_buhin2",
        original_item="key_w_buhin2"
    ),
    "Wildlands - Poltae Gold Metal Fragment": LRFF13LocationData(
        region="Wildlands",
        address=277,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_buhin3",
        original_item="key_w_buhin3"
    ),
    "Wildlands - Research Camp Data Recorder": LRFF13LocationData(
        region="Wildlands",
        address=278,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_data",
        original_item="key_w_data"
    ),
    "Wildlands - Aryas Village Apple (1)": LRFF13LocationData(
        region="Wildlands",
        address=279,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_apple1",
        original_item="key_w_apple"
    ),
    "Wildlands - Aryas Village Apple (2)": LRFF13LocationData(
        region="Wildlands",
        address=280,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_apple2",
        original_item="key_w_apple"
    ),
    "Wildlands - Aryas Village Apple (3)": LRFF13LocationData(
        region="Wildlands",
        address=281,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_w_apple3",
        original_item="key_w_apple"
    ),
    "Wildlands - Wildlands Boss Drop": LRFF13LocationData(
        region="Wildlands",
        address=282,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_wea_oa02",
        original_item="wea_oa02"
    ),
    "Wildlands - Wildlands Boss Reward (1)": LRFF13LocationData(
        region="Wildlands",
        address=283,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9030",
        original_item="key_r_atb"
    ),
    "Wildlands - Wildlands Boss Reward (2)": LRFF13LocationData(
        region="Wildlands",
        address=284,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9030_2",
        original_item="key_r_rec"
    ),
    "Yusnaan - Reveler's Quarter Lapis Lazuli Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=285,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_002",
        original_item="key_b_02"
    ),
    "Yusnaan - Industrial Area Power Booster": LRFF13LocationData(
        region="Yusnaan",
        address=286,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_003",
        original_item="key_b_03"
    ),
    "Yusnaan - Tunnel Oath of the Merchants Guild Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=287,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_012",
        original_item="key_b_12"
    ),
    "Yusnaan - Industrial Area Jade Hair Comb": LRFF13LocationData(
        region="Yusnaan",
        address=288,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_013",
        original_item="key_b_16"
    ),
    "Yusnaan - Industrial Area Bronze Pocket Watch": LRFF13LocationData(
        region="Yusnaan",
        address=289,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_b_014",
        original_item="key_b_17"
    ),
    "Yusnaan - Chocobo Girl Poster": LRFF13LocationData(
        region="Yusnaan",
        address=290,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_b_20",
        original_item="key_b_20"
    ),
    "Yusnaan - Glutton's Quarter Treasure (1)": LRFF13LocationData(
        region="Yusnaan",
        address=291,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_000",
        original_item="acc_a_3020"
    ),
    "Yusnaan - Aromatic Market Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=292,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_001",
        original_item="acc_a_0030"
    ),
    "Yusnaan - Central Ave Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=293,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_002",
        original_item="libra_m079"
    ),
    "Yusnaan - Coliseum Square Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=294,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_003",
        original_item="mg240_00_10"
    ),
    "Yusnaan - Tour Guide Sneaking-In Special Ticket": LRFF13LocationData(
        region="Yusnaan",
        address=295,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="trd_ticket",
        original_item="key_y_ticket"
    ),
    "Yusnaan - Warehouse District Id Card": LRFF13LocationData(
        region="Yusnaan",
        address=296,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_004",
        original_item="key_y_id"
    ),
    "Yusnaan - Coliseum Square (Musical) Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=297,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_005",
        original_item="key_y_kagi2"
    ),
    "Yusnaan - Cactuar Statue (Musical) Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=298,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_006",
        original_item="key_y_kagi3"
    ),
    "Yusnaan - Station (Musical) Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=299,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_007",
        original_item="key_y_rappa"
    ),
    "Yusnaan - Cactuar Statue Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=300,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_008",
        original_item="libra_m292"
    ),
    "Yusnaan - Reveler's Quarter Treasure (1)": LRFF13LocationData(
        region="Yusnaan",
        address=301,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_009",
        original_item="acc_b_4120"
    ),
    "Yusnaan - Augur's Quarter Treasure (1)": LRFF13LocationData(
        region="Yusnaan",
        address=302,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_010",
        original_item="acc_a_5010"
    ),
    "Yusnaan - Patron's Palace Treasure (1)": LRFF13LocationData(
        region="Yusnaan",
        address=303,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_011",
        original_item="acc_b_6200"
    ),
    "Yusnaan - Hawker's Row Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=304,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_012",
        original_item="at520_00_10"
    ),
    "Yusnaan - Augur's Quarter Treasure (2)": LRFF13LocationData(
        region="Yusnaan",
        address=305,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_013",
        original_item="acc_b_6210"
    ),
    "Yusnaan - Warehouse District Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=306,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_015",
        original_item="acc_a_8410"
    ),
    "Yusnaan - Augur's Quarter Treasure (3)": LRFF13LocationData(
        region="Yusnaan",
        address=307,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_017",
        original_item="acc_a_8000"
    ),
    "Yusnaan - Supply Line Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=308,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_018",
        original_item="acc_a_1000"
    ),
    "Yusnaan - Industrial Area Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=309,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_019",
        original_item="acc_a_8200"
    ),
    "Yusnaan - Lower City Treasure": LRFF13LocationData(
        region="Yusnaan",
        address=310,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_021",
        original_item="acc_b_4110"
    ),
    "Yusnaan - Glutton's Quarter Treasure (2)": LRFF13LocationData(
        region="Yusnaan",
        address=311,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_022",
        original_item="acc_a_8310"
    ),
    "Yusnaan - Reveler's Quarter Treasure (2)": LRFF13LocationData(
        region="Yusnaan",
        address=312,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_024",
        original_item="acc_b_6120"
    ),
    "Yusnaan - Patron's Palace Treasure (2)": LRFF13LocationData(
        region="Yusnaan",
        address=313,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_051",
        original_item="at010_10_10"
    ),
    "Yusnaan - Patron's Palace Treasure (3)": LRFF13LocationData(
        region="Yusnaan",
        address=314,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_052",
        original_item="gd040_00_10"
    ),
    "Yusnaan - Patron's Palace Treasure (4)": LRFF13LocationData(
        region="Yusnaan",
        address=315,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_055",
        original_item="acc_a_1110"
    ),
    "Yusnaan - Patron's Palace Treasure (5)": LRFF13LocationData(
        region="Yusnaan",
        address=316,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_056",
        original_item="libra_m381"
    ),
    "Yusnaan - Slaughterhouse Special Fragment of Courage": LRFF13LocationData(
        region="Yusnaan",
        address=317,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_y_059",
        original_item="key_s_kanki"
    ),
    "Yusnaan - Slaughterhouse (1)": LRFF13LocationData(
        region="Yusnaan",
        address=318,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_004",
        original_item="it_grace"
    ),
    "Yusnaan - Slaughterhouse (2)": LRFF13LocationData(
        region="Yusnaan",
        address=319,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_005",
        original_item="it_haste"
    ),
    "Yusnaan - Slaughterhouse (3)": LRFF13LocationData(
        region="Yusnaan",
        address=320,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_006",
        original_item="gil_l_000"
    ),
    "Yusnaan - Slaughterhouse (4)": LRFF13LocationData(
        region="Yusnaan",
        address=321,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_007",
        original_item="gil_l_010"
    ),
    "Yusnaan - Slaughterhouse (5)": LRFF13LocationData(
        region="Yusnaan",
        address=322,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_008",
        original_item="it_grace"
    ),
    "Yusnaan - Slaughterhouse (6)": LRFF13LocationData(
        region="Yusnaan",
        address=323,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_009",
        original_item="it_lowelxr"
    ),
    "Yusnaan - Slaughterhouse (7)": LRFF13LocationData(
        region="Yusnaan",
        address=324,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_010",
        original_item="gil_l_010"
    ),
    "Yusnaan - Slaughterhouse (8)": LRFF13LocationData(
        region="Yusnaan",
        address=325,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_012",
        original_item="it_haste"
    ),
    "Yusnaan - Slaughterhouse (9)": LRFF13LocationData(
        region="Yusnaan",
        address=326,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_013",
        original_item="it_upper"
    ),
    "Yusnaan - Slaughterhouse (10)": LRFF13LocationData(
        region="Yusnaan",
        address=327,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_col_y_014",
        original_item="gil_l_010"
    ),
    "Yusnaan - The Fighting Actress Slaughterhouse (1)": LRFF13LocationData(
        region="Yusnaan",
        address=328,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_col_y_016",
        original_item="gil_l_000"
    ),
    "Yusnaan - The Fighting Actress Slaughterhouse (2)": LRFF13LocationData(
        region="Yusnaan",
        address=329,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_col_y_017",
        original_item="gil_l_010"
    ),
    "Yusnaan - The Fighting Actress Slaughterhouse (3)": LRFF13LocationData(
        region="Yusnaan",
        address=330,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_col_y_018",
        original_item="gil_l_020"
    ),
    "Yusnaan - The Fighting Actress Slaughterhouse (4)": LRFF13LocationData(
        region="Yusnaan",
        address=331,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_cos_fa00",
        original_item="cos_fa00"
    ),
    "Yusnaan - Tanbam's Taboo Slaughterhouse": LRFF13LocationData(
        region="Yusnaan",
        address=332,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_col_y_019",
        original_item="gil_l_020"
    ),
    "Yusnaan - Chocobo Girl Miqo'te Dress": LRFF13LocationData(
        region="Yusnaan",
        address=333,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_cos_la00",
        original_item="cos_la00"
    ),
    "Yusnaan - Director Femme Fetale": LRFF13LocationData(
        region="Yusnaan",
        address=334,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_wea_da00",
        original_item="wea_da00"
    ),
    "Yusnaan - Fireworks in a Bottle Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=335,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_061"
    ),
    "Yusnaan - Fireworks in a Bottle Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=336,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_061_2",
        original_item="e318"
    ),
    "Yusnaan - The Fighting Actress Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=337,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_062"
    ),
    "Yusnaan - The Fighting Actress Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=338,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_062_2",
        original_item="e562"
    ),
    "Yusnaan - The Fighting Actress Quest (3)": LRFF13LocationData(
        region="Yusnaan",
        address=339,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_062_3",
        original_item="key_r_ep"
    ),
    "Yusnaan - Songless Diva Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=340,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_063"
    ),
    "Yusnaan - Songless Diva Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=341,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_063_2",
        original_item="e323"
    ),
    "Yusnaan - Stolen Things Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=342,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_064"
    ),
    "Yusnaan - Stolen Things Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=343,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_064_2",
        original_item="e315"
    ),
    "Yusnaan - Fireworks for a Steal Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=344,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_065"
    ),
    "Yusnaan - Fireworks for a Steal Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=345,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_065_2",
        original_item="e236"
    ),
    "Yusnaan - A Testing Proposition Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=346,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_066"
    ),
    "Yusnaan - A Testing Proposition Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=347,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_066_2",
        original_item="e033"
    ),
    "Yusnaan - Last Date Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=348,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_067"
    ),
    "Yusnaan - Last Date Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=349,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_qst_067_2",
        original_item="e048"
    ),
    "Yusnaan - Free Will Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=350,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_068"
    ),
    "Yusnaan - Free Will Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=351,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_068_2",
        original_item="cos_ea02"
    ),
    "Yusnaan - Free Will Quest (3)": LRFF13LocationData(
        region="Yusnaan",
        address=352,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_068_3",
        original_item="e042"
    ),
    "Yusnaan - Friends Forever Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=353,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_069"
    ),
    "Yusnaan - Friends Forever Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=354,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_069_2",
        original_item="e604"
    ),
    "Yusnaan - Friends Forever Quest (3)": LRFF13LocationData(
        region="Yusnaan",
        address=355,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_069_3",
        original_item="e309"
    ),
    "Yusnaan - Family Food Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=356,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_070"
    ),
    "Yusnaan - Family Food Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=357,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_070_2",
        original_item="e034"
    ),
    "Yusnaan - Tanbam's Taboo Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=358,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_071"
    ),
    "Yusnaan - Tanbam's Taboo Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=359,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_071_2",
        original_item="e308"
    ),
    "Yusnaan - Play It for Me Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=360,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_072"
    ),
    "Yusnaan - Play It for Me Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=361,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_072_2",
        original_item="e560"
    ),
    "Yusnaan - Adoring Adornments Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=362,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_073"
    ),
    "Yusnaan - Adoring Adornments Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=363,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_073_2",
        original_item="e246"
    ),
    "Yusnaan - Adoring Candice Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=364,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_074"
    ),
    "Yusnaan - Adoring Candice Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=365,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_074_2",
        original_item="e520"
    ),
    "Yusnaan - Adoring Candice Quest (3)": LRFF13LocationData(
        region="Yusnaan",
        address=366,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_074_3",
        original_item="e038"
    ),
    "Yusnaan - Death Safari Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=367,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_076"
    ),
    "Yusnaan - Death Safari Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=368,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_076_2",
        original_item="e578"
    ),
    "Yusnaan - Death Safari Quest (3)": LRFF13LocationData(
        region="Yusnaan",
        address=369,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_076_3",
        original_item="e579"
    ),
    "Yusnaan - Death Safari Quest (4)": LRFF13LocationData(
        region="Yusnaan",
        address=370,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_076_4",
        original_item="e580"
    ),
    "Yusnaan - Death Safari Quest (5)": LRFF13LocationData(
        region="Yusnaan",
        address=371,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_076_5",
        original_item="e581"
    ),
    "Yusnaan - Death Game Quest (1)": LRFF13LocationData(
        region="Yusnaan",
        address=372,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_077"
    ),
    "Yusnaan - Death Game Quest (2)": LRFF13LocationData(
        region="Yusnaan",
        address=373,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_077_2",
        original_item="cos_ka00"
    ),
    "Yusnaan - Death Game Quest (3)": LRFF13LocationData(
        region="Yusnaan",
        address=374,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_077_3",
        original_item="e264"
    ),
    "Yusnaan - Morris Musical Treasure Sphere Key": LRFF13LocationData(
        region="Yusnaan",
        address=375,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_y_kagi1",
        original_item="key_y_kagi1"
    ),
    "Yusnaan - Patron's Palace Serah's Pendant": LRFF13LocationData(
        region="Yusnaan",
        address=376,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_y_serap",
        original_item="key_y_serap"
    ),
    "Yusnaan - Gordon Gourmet's Recipe": LRFF13LocationData(
        region="Yusnaan",
        address=377,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_y_recipe",
        original_item="key_y_recipe"
    ),
    "Yusnaan - Seedy Steak a la Civet": LRFF13LocationData(
        region="Yusnaan",
        address=378,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_y_cream",
        original_item="key_y_cream"
    ),
    "Yusnaan - Gregory Father's Letter": LRFF13LocationData(
        region="Yusnaan",
        address=379,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_y_letter",
        original_item="key_y_letter"
    ),
    "Yusnaan - Tanbam's Taboo Libra Notes": LRFF13LocationData(
        region="Yusnaan",
        address=380,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_libra_m330",
        original_item="libra_m330"
    ),
    "Yusnaan - Yusnaan Boss Drop": LRFF13LocationData(
        region="Yusnaan",
        address=381,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9050",
        original_item="acc_a_9050"
    ),
    "Yusnaan - Yusnaan Boss Reward (1)": LRFF13LocationData(
        region="Yusnaan",
        address=382,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9010",
        original_item="key_r_ep"
    ),
    "Yusnaan - Yusnaan Boss Reward (2)": LRFF13LocationData(
        region="Yusnaan",
        address=383,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_9010_2",
        original_item="key_r_atb"
    ),
    "Ark - Initial 3rd Garb (1)": LRFF13LocationData(
        region="Ark",
        address=384,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_003",
        original_item="cos_ja00"
    ),
    "Ark - Initial 3rd Garb (2)": LRFF13LocationData(
        region="Ark",
        address=385,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_200",
        original_item="wea_fa00"
    ),
    "Ark - Initial 3rd Garb (3)": LRFF13LocationData(
        region="Ark",
        address=386,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_201",
        original_item="shi_ba00"
    ),
    "Ark - Ark Day 1 (1)": LRFF13LocationData(
        region="Ark",
        address=387,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_000",
        original_item="key_p_toppa"
    ),
    "Ark - Ark Day 1 (2)": LRFF13LocationData(
        region="Ark",
        address=388,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_a_pass1",
        original_item="key_r_ypass"
    ),
    "Ark - Ark Day 1 (3)": LRFF13LocationData(
        region="Ark",
        address=389,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_001",
        original_item="mat_cus_0_00"
    ),
    "Ark - Ark Day 1 (4)": LRFF13LocationData(
        region="Ark",
        address=390,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_a_pass2",
        original_item="key_r_wpass"
    ),
    "Ark - Ark Day 1 (5)": LRFF13LocationData(
        region="Ark",
        address=391,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_002",
        original_item="mat_abi_0_02"
    ),
    "Ark - Ark Day 1 (6)": LRFF13LocationData(
        region="Ark",
        address=392,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_a_pass3",
        original_item="key_r_dpass"
    ),
    "Ark - Ark Day 1 (7)": LRFF13LocationData(
        region="Ark",
        address=393,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_004",
        original_item="mb100_00_00"
    ),
    "Ark - Ark Day 1 (8)": LRFF13LocationData(
        region="Ark",
        address=394,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_004_2",
        original_item="gd030_00_00"
    ),
    "Ark - Ark Day 2 (1)": LRFF13LocationData(
        region="Ark",
        address=395,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_100",
        original_item="cos_ga06"
    ),
    "Ark - Ark Day 2 (2)": LRFF13LocationData(
        region="Ark",
        address=396,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_100_2",
        original_item="wea_ea01"
    ),
    "Ark - Ark Day 2 (3)": LRFF13LocationData(
        region="Ark",
        address=397,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_100_3",
        original_item="shi_ea02"
    ),
    "Ark - Ark Day 3 (1)": LRFF13LocationData(
        region="Ark",
        address=398,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_101",
        original_item="ti020_00"
    ),
    "Ark - Ark Day 4 (1)": LRFF13LocationData(
        region="Ark",
        address=399,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_102",
        original_item="cos_da06"
    ),
    "Ark - Ark Day 4 (2)": LRFF13LocationData(
        region="Ark",
        address=400,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_102_2",
        original_item="cos_ea01"
    ),
    "Ark - Ark Day 5 (1)": LRFF13LocationData(
        region="Ark",
        address=401,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_103",
        original_item="ti030_00"
    ),
    "Ark - Ark Day 6 (1)": LRFF13LocationData(
        region="Ark",
        address=402,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_104",
        original_item="mat_abi_0_00"
    ),
    "Ark - Ark Day 7": LRFF13LocationData(
        region="Ark",
        address=403,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_105",
        original_item="cos_ja06"
    ),
    "Ark - Ark Day 8": LRFF13LocationData(
        region="Ark",
        address=404,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_106",
        original_item="at900_00"
    ),
    "Ark - Ark Day 9": LRFF13LocationData(
        region="Ark",
        address=405,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_p_107",
        original_item="cos_ia00"
    ),
    "Ark - Ark Day 10": LRFF13LocationData(
        region="Ark",
        address=406,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_p_108",
        original_item="ti600_00"
    ),
    "Ark - Ark Day 11": LRFF13LocationData(
        region="Ark",
        address=407,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_p_109",
        original_item="cos_da04"
    ),
    "Ark - Ark Day 12": LRFF13LocationData(
        region="Ark",
        address=408,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_p_110",
        original_item="ti500_00"
    ),
    "Ark - Ark Final Day (1)": LRFF13LocationData(
        region="Ark",
        address=409,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_p_111",
        original_item="cos_ba08"
    ),
    "Ark - Ark Final Day (2)": LRFF13LocationData(
        region="Ark",
        address=410,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_p_111_2",
        original_item="cos_ca08"
    ),
    "Ark - Ark Final Day (3)": LRFF13LocationData(
        region="Ark",
        address=411,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_p_111_3",
        original_item="cos_ja08"
    ),
    "Ark - Ark Extra Day": LRFF13LocationData(
        region="Ark",
        address=412,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_p_112",
        original_item="mat_abi_0_01"
    ),
    "Ark - Replace Curaga": LRFF13LocationData(
        region="Ark",
        address=413,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_ti000",
        original_item="ti000_00"
    ),
    "Ark - Replace Teleport": LRFF13LocationData(
        region="Ark",
        address=414,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_ti810",
        original_item="ti810_00"
    ),
    "Ark - Replace Escape": LRFF13LocationData(
        region="Ark",
        address=415,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_ti830",
        original_item="ti830_00"
    ),
    "CoP Dead Dunes - Flower in the Sands CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=416,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1151"
    ),
    "CoP Dead Dunes - Flower in the Sands CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=417,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1151_1",
        original_item="e271"
    ),
    "CoP Dead Dunes - Biologically Speaking CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=418,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1152"
    ),
    "CoP Dead Dunes - Biologically Speaking CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=419,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1152_1",
        original_item="e293"
    ),
    "CoP Dead Dunes - The Real Client CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=420,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1153"
    ),
    "CoP Dead Dunes - The Real Client CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=421,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1153_1",
        original_item="e314"
    ),
    "CoP Dead Dunes - The Real Client CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=422,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1153_2",
        original_item="e329"
    ),
    "CoP Dead Dunes - For My Child CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=423,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1154"
    ),
    "CoP Dead Dunes - For My Child CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=424,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1154_1",
        original_item="e090"
    ),
    "CoP Dead Dunes - For My Child CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=425,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1154_2",
        original_item="e319"
    ),
    "CoP Dead Dunes - Bandits' New Weapon CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=426,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1155"
    ),
    "CoP Dead Dunes - Bandits' New Weapon CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=427,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1155_1",
        original_item="e342"
    ),
    "CoP Dead Dunes - Bandits' New Weapon CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=428,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1155_2",
        original_item="e311"
    ),
    "CoP Dead Dunes - Banned Goods CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=429,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1156"
    ),
    "CoP Dead Dunes - Banned Goods CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=430,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1156_1",
        original_item="e326"
    ),
    "CoP Dead Dunes - Banned Goods CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=431,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1156_2",
        original_item="e328"
    ),
    "CoP Dead Dunes - Climbing The Ranks I CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=432,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1157"
    ),
    "CoP Dead Dunes - Climbing The Ranks I CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=433,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1157_1",
        original_item="e297"
    ),
    "CoP Dead Dunes - Miracle Vintage CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=434,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1159"
    ),
    "CoP Dead Dunes - Miracle Vintage CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=435,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1159_1",
        original_item="e239"
    ),
    "CoP Dead Dunes - Miracle Vintage CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=436,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1159_2",
        original_item="e069"
    ),
    "CoP Dead Dunes - Climbing The Ranks II CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=437,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1164"
    ),
    "CoP Dead Dunes - Climbing The Ranks II CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=438,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1164_1",
        original_item="e272"
    ),
    "CoP Dead Dunes - Heightened Security CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=439,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1165"
    ),
    "CoP Dead Dunes - Heightened Security CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=440,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1165_1",
        original_item="e335"
    ),
    "CoP Dead Dunes - Heightened Security CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=441,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1165_2",
        original_item="e103"
    ),
    "CoP Dead Dunes - Desert Cleanup CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=442,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1168"
    ),
    "CoP Dead Dunes - Desert Cleanup CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=443,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1168_1",
        original_item="e050"
    ),
    "CoP Dead Dunes - Desert Cleanup CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=444,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1168_2",
        original_item="it_atel"
    ),
    "CoP Dead Dunes - A Treasure for a God CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=445,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1171"
    ),
    "CoP Dead Dunes - A Treasure for a God CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=446,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1171_1",
        original_item="e231"
    ),
    "CoP Dead Dunes - Lucky Charm CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=447,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1172"
    ),
    "CoP Dead Dunes - Lucky Charm CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=448,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1172_1",
        original_item="e044"
    ),
    "CoP Dead Dunes - Supply and Demand CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=449,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1173"
    ),
    "CoP Dead Dunes - Supply and Demand CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=450,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1173_1",
        original_item="e248"
    ),
    "CoP Dead Dunes - Supply and Demand CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=451,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1173_2",
        original_item="e704"
    ),
    "CoP Dead Dunes - A New Application CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=452,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1174"
    ),
    "CoP Dead Dunes - A New Application CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=453,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1174_1",
        original_item="e250"
    ),
    "CoP Dead Dunes - A New Application CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=454,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1174_2",
        original_item="e247"
    ),
    "CoP Dead Dunes - Pride And Greed I CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=455,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1175"
    ),
    "CoP Dead Dunes - Pride And Greed I CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=456,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1175_1",
        original_item="e268"
    ),
    "CoP Dead Dunes - Pride And Greed I CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=457,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1175_2",
        original_item="e273"
    ),
    "CoP Dead Dunes - Pride And Greed II CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=458,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1176"
    ),
    "CoP Dead Dunes - Pride And Greed II CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=459,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1176_1",
        original_item="e254"
    ),
    "CoP Dead Dunes - Pride And Greed II CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=460,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1176_2",
        original_item="e322"
    ),
    "CoP Dead Dunes - Pride And Greed III CoP Quest (1)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=461,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1177"
    ),
    "CoP Dead Dunes - Pride And Greed III CoP Quest (2)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=462,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1177_1",
        original_item="e080"
    ),
    "CoP Dead Dunes - Pride And Greed III CoP Quest (3)": LRFF13LocationData(
        region="CoP Dead Dunes",
        address=463,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1177_2",
        original_item="e294"
    ),
    "CoP Luxerion - Revenge Is Sweet CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=464,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1001"
    ),
    "CoP Luxerion - Revenge Is Sweet CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=465,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1001_1",
        original_item="e014"
    ),
    "CoP Luxerion - Gift of Gratitude CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=466,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1002"
    ),
    "CoP Luxerion - Gift of Gratitude CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=467,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1002_1",
        original_item="e065"
    ),
    "CoP Luxerion - Gift of Gratitude CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=468,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1002_2",
        original_item="e066"
    ),
    "CoP Luxerion - A Song for God CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=469,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1003"
    ),
    "CoP Luxerion - A Song for God CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=470,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1003_1",
        original_item="e227"
    ),
    "CoP Luxerion - A Song for God CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=471,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1003_2",
        original_item="e245"
    ),
    "CoP Luxerion - Slay the Machine CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=472,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1005"
    ),
    "CoP Luxerion - Slay the Machine CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=473,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1005_1",
        original_item="e298"
    ),
    "CoP Luxerion - Enchanted Brush CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=474,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1006"
    ),
    "CoP Luxerion - Enchanted Brush CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=475,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1006_1",
        original_item="e345"
    ),
    "CoP Luxerion - Enchanted Brush CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=476,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1006_2",
        original_item="e237"
    ),
    "CoP Luxerion - Heretics' Beasts CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=477,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1007"
    ),
    "CoP Luxerion - Heretics' Beasts CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=478,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1007_1",
        original_item="e263"
    ),
    "CoP Luxerion - Heretics' Beasts CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=479,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1007_2",
        original_item="e249"
    ),
    "CoP Luxerion - Grave of a Bounty Hunter CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=480,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1008"
    ),
    "CoP Luxerion - Grave of a Bounty Hunter CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=481,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1008_1",
        original_item="e259"
    ),
    "CoP Luxerion - Grave of a Bounty Hunter CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=482,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1008_2",
        original_item="e253"
    ),
    "CoP Luxerion - Inventive Seamstress CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=483,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1009"
    ),
    "CoP Luxerion - Inventive Seamstress CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=484,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1009_1",
        original_item="e207"
    ),
    "CoP Luxerion - Puppeteer's Lament CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=485,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1011"
    ),
    "CoP Luxerion - Puppeteer's Lament CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=486,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1011_1",
        original_item="e222"
    ),
    "CoP Luxerion - Puppeteer's Lament CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=487,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1011_2",
        original_item="e013"
    ),
    "CoP Luxerion - Revenge Has Teeth CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=488,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1012"
    ),
    "CoP Luxerion - Revenge Has Teeth CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=489,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1012_1",
        original_item="e333"
    ),
    "CoP Luxerion - Night Patrol CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=490,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1015"
    ),
    "CoP Luxerion - Night Patrol CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=491,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1015_1",
        original_item="e334"
    ),
    "CoP Luxerion - Night Patrol CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=492,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1015_2",
        original_item="e270"
    ),
    "CoP Luxerion - Trapped CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=493,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1016"
    ),
    "CoP Luxerion - Trapped CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=494,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1016_1",
        original_item="e053"
    ),
    "CoP Luxerion - Trapped CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=495,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1016_2",
        original_item="e049"
    ),
    "CoP Luxerion - Trapped CoP Quest (4)": LRFF13LocationData(
        region="CoP Luxerion",
        address=496,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1016_3",
        original_item="it_atel"
    ),
    "CoP Luxerion - Mythical Badge CoP Quest (1)": LRFF13LocationData(
        region="CoP Luxerion",
        address=497,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1021"
    ),
    "CoP Luxerion - Mythical Badge CoP Quest (2)": LRFF13LocationData(
        region="CoP Luxerion",
        address=498,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1021_1",
        original_item="e240"
    ),
    "CoP Luxerion - Mythical Badge CoP Quest (3)": LRFF13LocationData(
        region="CoP Luxerion",
        address=499,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1021_2",
        original_item="e060"
    ),
    "CoP Wildlands - Sun Flower CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=500,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1101"
    ),
    "CoP Wildlands - Sun Flower CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=501,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1101_1",
        original_item="e302"
    ),
    "CoP Wildlands - Moon Flower CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=502,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1102"
    ),
    "CoP Wildlands - Moon Flower CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=503,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1102_1",
        original_item="e200"
    ),
    "CoP Wildlands - Moon Flower CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=504,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1102_2",
        original_item="e204"
    ),
    "CoP Wildlands - Secret of the Chocoborel CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=505,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1103"
    ),
    "CoP Wildlands - Secret of the Chocoborel CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=506,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1103_1",
        original_item="e213"
    ),
    "CoP Wildlands - Secret of the Chocoborel CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=507,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1103_2",
        original_item="e214"
    ),
    "CoP Wildlands - Wildlands In Danger! CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=508,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1104"
    ),
    "CoP Wildlands - Wildlands In Danger! CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=509,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1104_1",
        original_item="e074"
    ),
    "CoP Wildlands - Wildlands In Danger! CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=510,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1104_2",
        original_item="e078"
    ),
    "CoP Wildlands - Hunting the Hunter CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=511,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1105"
    ),
    "CoP Wildlands - Hunting the Hunter CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=512,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1105_1",
        original_item="e278"
    ),
    "CoP Wildlands - Hunting the Hunter CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=513,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1105_2",
        original_item="e279"
    ),
    "CoP Wildlands - Forget Me Not CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=514,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1106"
    ),
    "CoP Wildlands - Forget Me Not CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=515,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1106_1",
        original_item="e208"
    ),
    "CoP Wildlands - Forget Me Not CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=516,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1106_2",
        original_item="e305"
    ),
    "CoP Wildlands - A Word of Thanks CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=517,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1107"
    ),
    "CoP Wildlands - A Word of Thanks CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=518,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1107_1",
        original_item="e210"
    ),
    "CoP Wildlands - A Word of Thanks CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=519,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1107_2",
        original_item="e211"
    ),
    "CoP Wildlands - Fresh Fertilizer CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=520,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1108"
    ),
    "CoP Wildlands - Fresh Fertilizer CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=521,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1108_1",
        original_item="e004"
    ),
    "CoP Wildlands - Fresh Fertilizer CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=522,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1108_2",
        original_item="e706"
    ),
    "CoP Wildlands - For the Future CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=523,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1109"
    ),
    "CoP Wildlands - For the Future CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=524,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1109_1",
        original_item="e344"
    ),
    "CoP Wildlands - For the Future CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=525,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1109_2",
        original_item="e266"
    ),
    "CoP Wildlands - Dumpling Cook-Off CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=526,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1110"
    ),
    "CoP Wildlands - Dumpling Cook-Off CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=527,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1110_1",
        original_item="e296"
    ),
    "CoP Wildlands - Dumpling Cook-Off CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=528,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1110_2",
        original_item="e275"
    ),
    "CoP Wildlands - Brain Over Brawn CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=529,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1111"
    ),
    "CoP Wildlands - Brain Over Brawn CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=530,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1111_1",
        original_item="e702"
    ),
    "CoP Wildlands - Brain Over Brawn CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=531,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1111_2",
        original_item="e707"
    ),
    "CoP Wildlands - Hunter's Challenge CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=532,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1113"
    ),
    "CoP Wildlands - Hunter's Challenge CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=533,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1113_1",
        original_item="e217"
    ),
    "CoP Wildlands - Hunter's Challenge CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=534,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1113_2",
        original_item="e215"
    ),
    "CoP Wildlands - A Secret Wish CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=535,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1114"
    ),
    "CoP Wildlands - A Secret Wish CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=536,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1114_1",
        original_item="e310"
    ),
    "CoP Wildlands - A Secret Wish CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=537,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1114_2",
        original_item="e256"
    ),
    "CoP Wildlands - Moghan's Plea CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=538,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1115"
    ),
    "CoP Wildlands - Moghan's Plea CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=539,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1115_1",
        original_item="e258"
    ),
    "CoP Wildlands - Moghan's Plea CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=540,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1115_2",
        original_item="e257"
    ),
    "CoP Wildlands - What's in a Brew? CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=541,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1116"
    ),
    "CoP Wildlands - What's in a Brew? CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=542,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1116_1",
        original_item="e280"
    ),
    "CoP Wildlands - What's in a Brew? CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=543,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1116_2",
        original_item="e282"
    ),
    "CoP Wildlands - What's in a Brew? CoP Quest (4)": LRFF13LocationData(
        region="CoP Wildlands",
        address=544,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1116_3",
        original_item="it_atel"
    ),
    "CoP Wildlands - A Prayer to a Goddess CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=545,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1117"
    ),
    "CoP Wildlands - A Prayer to a Goddess CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=546,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1117_1",
        original_item="e023"
    ),
    "CoP Wildlands - A Prayer to a Goddess CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=547,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1117_2",
        original_item="e067"
    ),
    "CoP Wildlands - Gatekeeper's Curiosity CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=548,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1118"
    ),
    "CoP Wildlands - Gatekeeper's Curiosity CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=549,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1118_1",
        original_item="e267"
    ),
    "CoP Wildlands - Echoes of a Drum CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=550,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1119"
    ),
    "CoP Wildlands - Echoes of a Drum CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=551,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1119_1",
        original_item="e327"
    ),
    "CoP Wildlands - Echoes of a Drum CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=552,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1119_2",
        original_item="e325"
    ),
    "CoP Wildlands - A Voice From Below CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=553,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1120"
    ),
    "CoP Wildlands - A Voice From Below CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=554,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1120_1",
        original_item="e317"
    ),
    "CoP Wildlands - A Voice From Below CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=555,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1120_2",
        original_item="e233"
    ),
    "CoP Wildlands - Chocobo Chow CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=556,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1121"
    ),
    "CoP Wildlands - Chocobo Chow CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=557,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1121_1",
        original_item="e219"
    ),
    "CoP Wildlands - Chocobo Chow CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=558,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1121_2",
        original_item="e218"
    ),
    "CoP Wildlands - Sylkis Secrets CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=559,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1122"
    ),
    "CoP Wildlands - Sylkis Secrets CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=560,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1122_1",
        original_item="e260"
    ),
    "CoP Wildlands - Sylkis Secrets CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=561,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1122_2",
        original_item="e331"
    ),
    "CoP Wildlands - Digging Mole CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=562,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1123"
    ),
    "CoP Wildlands - Digging Mole CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=563,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1123_1",
        original_item="e220"
    ),
    "CoP Wildlands - Digging Mole CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=564,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1123_2",
        original_item="e072"
    ),
    "CoP Wildlands - Two Together CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=565,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1124"
    ),
    "CoP Wildlands - Two Together CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=566,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1124_1",
        original_item="e202"
    ),
    "CoP Wildlands - Two Together CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=567,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1124_2",
        original_item="e201"
    ),
    "CoP Wildlands - Emergency Treatment CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=568,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1125"
    ),
    "CoP Wildlands - Emergency Treatment CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=569,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1125_1",
        original_item="e289"
    ),
    "CoP Wildlands - Emergency Treatment CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=570,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1125_2",
        original_item="e287"
    ),
    "CoP Wildlands - Moogle Gourmand CoP Quest (1)": LRFF13LocationData(
        region="CoP Wildlands",
        address=571,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1126"
    ),
    "CoP Wildlands - Moogle Gourmand CoP Quest (2)": LRFF13LocationData(
        region="CoP Wildlands",
        address=572,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1126_1",
        original_item="e262"
    ),
    "CoP Wildlands - Moogle Gourmand CoP Quest (3)": LRFF13LocationData(
        region="CoP Wildlands",
        address=573,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1126_2",
        original_item="e288"
    ),
    "CoP Yusnaan - Secret Machine CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=574,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1051"
    ),
    "CoP Yusnaan - Secret Machine CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=575,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1051_1",
        original_item="e292"
    ),
    "CoP Yusnaan - Soulful Horn CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=576,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1052"
    ),
    "CoP Yusnaan - Soulful Horn CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=577,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1052_1",
        original_item="e234"
    ),
    "CoP Yusnaan - Soulful Horn CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=578,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1052_2",
        original_item="e238"
    ),
    "CoP Yusnaan - A Dangerous Cocktail CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=579,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1056"
    ),
    "CoP Yusnaan - A Dangerous Cocktail CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=580,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1056_1",
        original_item="e332"
    ),
    "CoP Yusnaan - Source of Inspiration CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=581,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1059"
    ),
    "CoP Yusnaan - Source of Inspiration CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=582,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1059_1",
        original_item="e226"
    ),
    "CoP Yusnaan - Youth Potion CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=583,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1060"
    ),
    "CoP Yusnaan - Youth Potion CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=584,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1060_1",
        original_item="e003"
    ),
    "CoP Yusnaan - Youth Potion CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=585,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1060_2",
        original_item="e303"
    ),
    "CoP Yusnaan - Beast Summoner CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=586,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1061"
    ),
    "CoP Yusnaan - Beast Summoner CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=587,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1061_1",
        original_item="e010"
    ),
    "CoP Yusnaan - Beast Summoner CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=588,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1061_2",
        original_item="e011"
    ),
    "CoP Yusnaan - What Seekers Seek CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=589,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1062"
    ),
    "CoP Yusnaan - What Seekers Seek CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=590,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1062_1",
        original_item="e235"
    ),
    "CoP Yusnaan - What Seekers Seek CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=591,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1062_2",
        original_item="e705"
    ),
    "CoP Yusnaan - True Colors CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=592,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1063"
    ),
    "CoP Yusnaan - True Colors CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=593,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1063_1",
        original_item="e251"
    ),
    "CoP Yusnaan - True Colors CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=594,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1063_2",
        original_item="e252"
    ),
    "CoP Yusnaan - Ultimate Craving CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=595,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1064"
    ),
    "CoP Yusnaan - Ultimate Craving CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=596,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1064_1",
        original_item="e016"
    ),
    "CoP Yusnaan - Ultimate Craving CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=597,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1064_2",
        original_item="e223"
    ),
    "CoP Yusnaan - Ultimate Craving CoP Quest (4)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=598,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1064_3",
        original_item="it_atel"
    ),
    "CoP Yusnaan - Spell for Spell CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=599,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1065"
    ),
    "CoP Yusnaan - Spell for Spell CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=600,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1065_1",
        original_item="e019"
    ),
    "CoP Yusnaan - Spell for Spell CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=601,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1065_2",
        original_item="e295"
    ),
    "CoP Yusnaan - Unfired Firework CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=602,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1071"
    ),
    "CoP Yusnaan - Unfired Firework CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=603,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1071_1",
        original_item="e243"
    ),
    "CoP Yusnaan - Unfired Firework CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=604,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1071_2",
        original_item="e073"
    ),
    "CoP Yusnaan - Time Doesn't Heal CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=605,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1072"
    ),
    "CoP Yusnaan - Time Doesn't Heal CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=606,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1072_1",
        original_item="e221"
    ),
    "CoP Yusnaan - Time Doesn't Heal CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=607,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1072_2",
        original_item="e061"
    ),
    "CoP Yusnaan - A Man for a Chocobo Girl CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=608,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1073"
    ),
    "CoP Yusnaan - A Man for a Chocobo Girl CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=609,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1073_1",
        original_item="e285"
    ),
    "CoP Yusnaan - A Man for a Chocobo Girl CoP Quest (3)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=610,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1073_2",
        original_item="e286"
    ),
    "CoP Yusnaan - Rebuilding CoP Quest (1)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=611,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1074"
    ),
    "CoP Yusnaan - Rebuilding CoP Quest (2)": LRFF13LocationData(
        region="CoP Yusnaan",
        address=612,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1074_1",
        original_item="e324"
    ),
    "CoP Global - Global: Key To Her Heart CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=613,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1301"
    ),
    "CoP Global - Global: Key To Her Heart CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=614,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1301_1",
        original_item="key_s_zyouai"
    ),
    "CoP Global - Global: Key To Her Heart CoP Quest (3)": LRFF13LocationData(
        region="CoP Global",
        address=615,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1301_2",
        original_item="e603"
    ),
    "CoP Global - Global: Roadworks I CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=616,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1302"
    ),
    "CoP Global - Global: Roadworks I CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=617,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1302_1",
        original_item="wea_la01"
    ),
    "CoP Global - Global: Roadworks I CoP Quest (3)": LRFF13LocationData(
        region="CoP Global",
        address=618,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1302_2",
        original_item="shi_ia01"
    ),
    "CoP Global - Global: Roadworks II CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=619,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1303"
    ),
    "CoP Global - Global: Roadworks II CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=620,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1303_1",
        original_item="wea_la02"
    ),
    "CoP Global - Global: Roadworks II CoP Quest (3)": LRFF13LocationData(
        region="CoP Global",
        address=621,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1303_2",
        original_item="shi_ia02"
    ),
    "CoP Global - Global: Roadworks III CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=622,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1304"
    ),
    "CoP Global - Global: Roadworks III CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=623,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1304_1",
        original_item="wea_la00"
    ),
    "CoP Global - Global: Roadworks III CoP Quest (3)": LRFF13LocationData(
        region="CoP Global",
        address=624,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1304_2",
        original_item="shi_ia00"
    ),
    "CoP Global - Global: A Girl's Challenge CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=625,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1305"
    ),
    "CoP Global - Global: A Girl's Challenge CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=626,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1305_1",
        original_item="e274"
    ),
    "CoP Global - Global: What's Left Behind CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=627,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1306"
    ),
    "CoP Global - Global: What's Left Behind CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=628,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1306_1",
        original_item="e203"
    ),
    "CoP Global - Global: Seeing The Dawn CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=629,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1307"
    ),
    "CoP Global - Global: Seeing The Dawn CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=630,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1307_1",
        original_item="e244"
    ),
    "CoP Global - Global: Staying Sharp CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=631,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1308"
    ),
    "CoP Global - Global: Staying Sharp CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=632,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1308_1",
        original_item="e306"
    ),
    "CoP Global - Global: Where Moogles Be CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=633,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1309"
    ),
    "CoP Global - Global: Where Moogles Be CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=634,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1309_1",
        original_item="e313"
    ),
    "CoP Global - Global: Fading Prayer CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=635,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1310"
    ),
    "CoP Global - Global: Fading Prayer CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=636,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1310_1",
        original_item="e052"
    ),
    "CoP Global - Global: Forbidden Tome CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=637,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1311"
    ),
    "CoP Global - Global: Forbidden Tome CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=638,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1311_1",
        original_item="e283"
    ),
    "CoP Global - Global: Shoot For The Sky CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=639,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1312"
    ),
    "CoP Global - Global: Shoot For The Sky CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=640,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1312_1",
        original_item="e209"
    ),
    "CoP Global - Global: Shoot For The Sky CoP Quest (3)": LRFF13LocationData(
        region="CoP Global",
        address=641,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1312_2",
        original_item="e098"
    ),
    "CoP Global - Global: Digging Mysteries CoP Quest (1)": LRFF13LocationData(
        region="CoP Global",
        address=642,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1313"
    ),
    "CoP Global - Global: Digging Mysteries CoP Quest (2)": LRFF13LocationData(
        region="CoP Global",
        address=643,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1313_1",
        original_item="e039"
    ),
    "CoP Global - Global: Digging Mysteries CoP Quest (3)": LRFF13LocationData(
        region="CoP Global",
        address=644,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_1313_2",
        original_item="e341"
    ),
    "Soul Seeds - 10 Soul Seeds": LRFF13LocationData(
        region="Soul Seeds",
        address=645,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_seed_1st_00",
        original_item="it_hero"
    ),
    "Soul Seeds - 20 Soul Seeds": LRFF13LocationData(
        region="Soul Seeds",
        address=646,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_seed_1st_01",
        original_item="it_war"
    ),
    "Soul Seeds - 30 Soul Seeds": LRFF13LocationData(
        region="Soul Seeds",
        address=647,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_seed_1st_02",
        original_item="it_atel"
    ),
    "Soul Seeds - 40 Soul Seeds": LRFF13LocationData(
        region="Soul Seeds",
        address=648,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_seed_1st_03",
        original_item="it_phenxbl"
    ),
    "Soul Seeds - 50 Soul Seeds": LRFF13LocationData(
        region="Soul Seeds",
        address=649,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_seed_1st_04",
        original_item="it_elixir"
    ),
    "Soul Seeds - Soul Seeds Fragment of Radiance": LRFF13LocationData(
        region="Soul Seeds",
        address=650,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_s_hiai",
        original_item="key_s_hiai"
    ),
    "Unappraised - 1 Unappraised": LRFF13LocationData(
        region="Unappraised",
        address=651,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_d_kant1",
        original_item="key_d_key"
    ),
    "Unappraised - 5 Unappraised": LRFF13LocationData(
        region="Unappraised",
        address=652,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_d_kant2",
        original_item="gil_r_000"
    ),
    "Unappraised - 10 Unappraised": LRFF13LocationData(
        region="Unappraised",
        address=653,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_d_kant3",
        original_item="it_atel"
    ),
    "Unappraised - 20 Unappraised": LRFF13LocationData(
        region="Unappraised",
        address=654,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_d_kant4",
        original_item="gil_r_010"
    ),
    "Unappraised - 50 Unappraised": LRFF13LocationData(
        region="Unappraised",
        address=655,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_key_d_kant5",
        original_item="it_hiatel"
    ),
    "Ultimate Lair - Floor 1 Hoplite Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=656,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9030",
        original_item="acc_b_9030"
    ),
    "Ultimate Lair - Floor 2 Niblet Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=657,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9090",
        original_item="acc_a_9090"
    ),
    "Ultimate Lair - Floor 3 Zaltys Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=658,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9010",
        original_item="acc_a_9010"
    ),
    "Ultimate Lair - Floor 4 Gaunt Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=659,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9050",
        original_item="acc_b_9050"
    ),
    "Ultimate Lair - Floor 5 Gremlin Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=660,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9080",
        original_item="acc_a_9080"
    ),
    "Ultimate Lair - Floor 6 Dreadnought Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=661,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9020",
        original_item="acc_b_9020"
    ),
    "Ultimate Lair - Floor 7 Gorgonopsid Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=662,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9000",
        original_item="acc_a_9000"
    ),
    "Ultimate Lair - Floor 8 Goblot Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=663,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9100",
        original_item="acc_a_9100"
    ),
    "Ultimate Lair - Floor 9 Gurangatch Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=664,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9220",
        original_item="acc_a_9220"
    ),
    "Ultimate Lair - Floor 10 Ectopudding Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=665,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9080",
        original_item="acc_b_9080"
    ),
    "Ultimate Lair - Floor 11 Miniflan Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=666,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9020",
        original_item="acc_a_9020"
    ),
    "Ultimate Lair - Floor 12 Aster Protoflorian Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=667,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9040",
        original_item="acc_b_9040"
    ),
    "Ultimate Lair - Floor 13 Schrodinger Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=668,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9120",
        original_item="acc_a_9120"
    ),
    "Ultimate Lair - Floor 14 Goblin Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=669,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9070",
        original_item="acc_a_9070"
    ),
    "Ultimate Lair - Floor 15 Reaver Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=670,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_wea_oa07",
        original_item="wea_oa07"
    ),
    "Ultimate Lair - Floor 16 Meonekton Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=671,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9090",
        original_item="acc_b_9090"
    ),
    "Ultimate Lair - Floor 17 Cactuar Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=672,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9190",
        original_item="acc_a_9190"
    ),
    "Ultimate Lair - Floor 18 Triffid Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=673,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9110",
        original_item="acc_a_9110"
    ),
    "Ultimate Lair - Floor 19 Cyclops Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=674,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_wea_oa05",
        original_item="wea_oa05"
    ),
    "Ultimate Lair - Floor 20 Skeleton Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=675,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_wea_oa13",
        original_item="wea_oa13"
    ),
    "Ultimate Lair - Floor 21 Desert Sahagin Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=676,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9150",
        original_item="acc_a_9150"
    ),
    "Ultimate Lair - Floor 22 Earth Eater Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=677,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9130",
        original_item="acc_a_9130"
    ),
    "Ultimate Lair - Floor 23 Skata'ne Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=678,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9000",
        original_item="acc_b_9000"
    ),
    "Ultimate Lair - Floor 24 Hanuman Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=679,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9030",
        original_item="acc_a_9030"
    ),
    "Ultimate Lair - Floor 25 Zomok Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=680,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9040",
        original_item="acc_a_9040"
    ),
    "Ultimate Lair - Floor 26 Dryad Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=681,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_b_9010",
        original_item="acc_b_9010"
    ),
    "Ultimate Lair - Floor 27 Rafflesia Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=682,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9180",
        original_item="acc_a_9180"
    ),
    "Ultimate Lair - Floor 28 Chocobo Eater Omega Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=683,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9140",
        original_item="acc_a_9140"
    ),
    "Ultimate Lair - Floor 29 UL Treasure": LRFF13LocationData(
        region="Ultimate Lair",
        address=684,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_e_000",
        original_item="it_expotion"
    ),
    "Ultimate Lair - Floor 30 UL Treasure": LRFF13LocationData(
        region="Ultimate Lair",
        address=685,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_e_001",
        original_item="it_lowelxr"
    ),
    "Ultimate Lair - Floor 31 UL Treasure": LRFF13LocationData(
        region="Ultimate Lair",
        address=686,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_e_002",
        original_item="it_phenxtal"
    ),
    "Ultimate Lair - Floor 32 UL Treasure": LRFF13LocationData(
        region="Ultimate Lair",
        address=687,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_box_e_003",
        original_item="it_atel"
    ),
    "Ultimate Lair - Ultimate Lair Boss Drop": LRFF13LocationData(
        region="Ultimate Lair",
        address=688,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_acc_a_9210",
        original_item="acc_a_9210"
    ),
    "Ultimate Lair - Ultimate Lair Boss Reward (1)": LRFF13LocationData(
        region="Ultimate Lair",
        address=689,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_099",
        original_item="cos_ba04"
    ),
    "Ultimate Lair - Ultimate Lair Boss Reward (2)": LRFF13LocationData(
        region="Ultimate Lair",
        address=690,
        classification=LocationProgressType.DEFAULT,
        type="treasure",
        str_id="tre_qst_099_2",
        original_item="key_r_atb"
    ),
    "Final Day - Arcangeli Omega Drop": LRFF13LocationData(
        region="Final Day",
        address=691,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_acc_b_9070",
        original_item="acc_b_9070"
    ),
    "Final Day - Sugriva Omega Drop": LRFF13LocationData(
        region="Final Day",
        address=692,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_acc_a_9160",
        original_item="acc_a_9160"
    ),
    "Final Day - Chimera Omega Drop": LRFF13LocationData(
        region="Final Day",
        address=693,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_acc_a_9170",
        original_item="acc_a_9170"
    ),
    "Final Day - Final Day Altar Of Salvation": LRFF13LocationData(
        region="Final Day",
        address=694,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_l_026",
        original_item="mb030_00_00"
    ),
    "Final Day - Final Day Altar Of Judgment": LRFF13LocationData(
        region="Final Day",
        address=695,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_l_027",
        original_item="mb130_00_00"
    ),
    "Final Day - Final Day Altar Of Atonement": LRFF13LocationData(
        region="Final Day",
        address=696,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_l_028",
        original_item="mb230_00_00"
    ),
    "Final Day - Final Day Altar Of Birth": LRFF13LocationData(
        region="Final Day",
        address=697,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_l_029",
        original_item="mb430_00_00"
    ),
    "Final Day - Final Day Temple Of Light (1)": LRFF13LocationData(
        region="Final Day",
        address=698,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_l_030",
        original_item="libra_m387"
    ),
    "Final Day - Final Day Temple Of Light (2)": LRFF13LocationData(
        region="Final Day",
        address=699,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_l_031",
        original_item="acc_a_0020"
    ),
    "Final Day - Final Day Temple Of Light (3)": LRFF13LocationData(
        region="Final Day",
        address=700,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_box_l_032",
        original_item="acc_a_1020"
    ),
    "Final Day - Final Day Ultima Weapon": LRFF13LocationData(
        region="Final Day",
        address=701,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_wea_ea00",
        original_item="wea_ea00"
    ),
    "Final Day - Final Day Ultima Shield": LRFF13LocationData(
        region="Final Day",
        address=702,
        classification=LocationProgressType.EXCLUDED,
        type="treasure",
        str_id="tre_shi_ea00",
        original_item="shi_ea00"
    ),
    "Dead Dunes - Cactair Fragment of Kindness": LRFF13LocationData(
        region="Dead Dunes",
        address=703,
        classification=LocationProgressType.DEFAULT,
        type="battle",
        str_id="btsc04902",
        original_item="key_s_hunnu"
    ),
    "Dead Dunes - Goblots Arithmometer": LRFF13LocationData(
        region="Dead Dunes",
        address=704,
        classification=LocationProgressType.DEFAULT,
        type="battle",
        str_id="btsc04900",
        original_item="key_d_keisan"
    ),
    "Dead Dunes - Aeronite Monster Flesh": LRFF13LocationData(
        region="Dead Dunes",
        address=705,
        classification=LocationProgressType.DEFAULT,
        type="battle",
        str_id="btsc04990",
        original_item="key_d_niku"
    ),
    "Luxerion - Zomok Cursed Dragon Claw": LRFF13LocationData(
        region="Luxerion",
        address=706,
        classification=LocationProgressType.DEFAULT,
        type="battle",
        str_id="btsc01900",
        original_item="key_behi_tume"
    ),
    "Yusnaan - Gremlins Music Satchel": LRFF13LocationData(
        region="Yusnaan",
        address=707,
        classification=LocationProgressType.DEFAULT,
        type="battle",
        str_id="btsc02902",
        original_item="key_y_kaban"
    ),
    "Yusnaan - Schrodinger Civet Musk": LRFF13LocationData(
        region="Yusnaan",
        address=708,
        classification=LocationProgressType.DEFAULT,
        type="battle",
        str_id="btsc02952",
        original_item="key_y_bashira"
    ),
}

location_table = {location_name: location_data.address for location_name, location_data in location_data_table.items()}