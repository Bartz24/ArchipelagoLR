from typing import Dict, List, NamedTuple, Optional
from BaseClasses import Region

class LRFF13Region(Region):
    game: str = "Lightning Returns: Final Fantasy XIII"

class LRFF13RegionData(NamedTuple):
    connecting_regions: List[str]
    map_id: Optional[int] = None
    secondary_index: Optional[int] = None

region_data_table: Dict[str, LRFF13RegionData] = {
    "Initial": LRFF13RegionData(connecting_regions=["Ark"], map_id=0),
    "Ark": LRFF13RegionData(connecting_regions=["Luxerion", "CoP Global", "Ultimate Lair", "Final Day"], map_id=1),
    "Luxerion": LRFF13RegionData(connecting_regions=["Dead Dunes", "Wildlands", "Yusnaan", "CoP Luxerion"], map_id=2),
    "Wildlands": LRFF13RegionData(connecting_regions=["CoP Wildlands"], map_id=3),
    "Dead Dunes": LRFF13RegionData(connecting_regions=["CoP Dead Dunes", "Soul Seeds/Unappraised"], map_id=4),
    "Yusnaan": LRFF13RegionData(connecting_regions=["CoP Yusnaan"], map_id=5),
    "CoP Dead Dunes": LRFF13RegionData(connecting_regions=[], map_id=6),
    "CoP Luxerion": LRFF13RegionData(connecting_regions=[], map_id=7),
    "CoP Wildlands": LRFF13RegionData(connecting_regions=[], map_id=8),
    "CoP Yusnaan": LRFF13RegionData(connecting_regions=[], map_id=9),
    "CoP Global": LRFF13RegionData(connecting_regions=[], map_id=10),
    "Soul Seeds/Unappraised": LRFF13RegionData(connecting_regions=[], map_id=11),
    "Ultimate Lair": LRFF13RegionData(connecting_regions=[], map_id=12),
    "Final Day": LRFF13RegionData(connecting_regions=[], map_id=13),
}
