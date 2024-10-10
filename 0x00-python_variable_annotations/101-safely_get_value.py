#!/usr/bin/env python3
from typing import Any, TypeVar, Dict

T = TypeVar('T')

def safely_get_value(dct: Dict[Any, T], key: Any, default: T = None) -> T:
    """
    Returns the value associated with the given key in the dictionary if the key exists, 
    otherwise returns the default value.

    Parameters:
    dct (Dict[Any, T]): The dictionary to retrieve the value from.
    key (Any): The key to look up in the dictionary.
    default (T): The value to return if the key is not found. Defaults to None.

    Returns:
    T: The value associated with the key, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
