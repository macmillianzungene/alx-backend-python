#!/usr/bin/env python3
from typing import Any, Optional, Sequence

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    This function accepts any sequence (list, tuple, etc.) and provides a safe way to
    retrieve the first element. If the sequence is empty, it returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
