#!/usr/bin/env python3
from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a list with each element in the input tuple repeated 'factor' times.

    Parameters:
    lst (Tuple[int, ...]): The input tuple.
    factor (int): The number of times each element should be repeated. Defaults to 2.

    Returns:
    List[int]: The list with repeated elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

