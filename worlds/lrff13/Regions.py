from typing import Dict, List, NamedTuple


class LRFF13RegionData(NamedTuple):
    connecting_regions: List[str] = []


# TODO: Switch to actually use the regions once the standalone randomizer uses regions as well.
region_data_table: Dict[str, LRFF13RegionData] = {
    "Menu": LRFF13RegionData(["Nova"]),
    "Nova": LRFF13RegionData(),
}
