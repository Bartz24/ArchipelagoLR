from typing import List
from .Items import item_data_table


def state_has_at_least(possible: List[bool], count: int) -> bool:
    # Returns true if at least count of the possible are true
    return possible.count(True) >= count

def item_is_category(item_name : str, category : str) -> bool:
    return item_data_table[item_name].category == category