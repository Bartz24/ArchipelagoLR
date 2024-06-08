from typing import List


def state_has_at_least(possible: List[bool], count: int) -> bool:
    # Returns true if at least count of the possible are true
    return possible.count(True) >= count