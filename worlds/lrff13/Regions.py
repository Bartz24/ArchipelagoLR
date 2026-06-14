from typing import Dict, List, NamedTuple, Optional
from BaseClasses import Region

class LRFF13Region(Region):
    game: str = "Lightning Returns: Final Fantasy XIII"

class LRFF13RegionData(NamedTuple):
    connecting_regions: List[str]
    map_id: Optional[int] = None
    secondary_index: Optional[int] = None

region_data_table: Dict[str, LRFF13RegionData] = {
    "Anywhere": LRFF13RegionData(connecting_regions=[]),
    "Ark": LRFF13RegionData(connecting_regions=["Anywhere", "CoP Global", "Final Day", "Luxerion", "Shops"]),
    "CoP Dead Dunes": LRFF13RegionData(connecting_regions=[]),
    "CoP Global": LRFF13RegionData(connecting_regions=[]),
    "CoP Luxerion": LRFF13RegionData(connecting_regions=[]),
    "CoP Wildlands": LRFF13RegionData(connecting_regions=[]),
    "CoP Yusnaan": LRFF13RegionData(connecting_regions=[]),
    "Dead Dunes": LRFF13RegionData(connecting_regions=["CoP Dead Dunes", "Ultimate Lair", "Unappraised"]),
    "Final Day": LRFF13RegionData(connecting_regions=[]),
    "Initial": LRFF13RegionData(connecting_regions=["Ark"]),
    "Luxerion": LRFF13RegionData(connecting_regions=["CoP Luxerion", "Dead Dunes", "Soul Seeds", "Wildlands", "Yusnaan"]),
    "Shops": LRFF13RegionData(connecting_regions=[]),
    "Soul Seeds": LRFF13RegionData(connecting_regions=[]),
    "Ultimate Lair": LRFF13RegionData(connecting_regions=[]),
    "Unappraised": LRFF13RegionData(connecting_regions=[]),
    "Wildlands": LRFF13RegionData(connecting_regions=["CoP Wildlands"]),
    "Yusnaan": LRFF13RegionData(connecting_regions=["CoP Yusnaan"]),
}
