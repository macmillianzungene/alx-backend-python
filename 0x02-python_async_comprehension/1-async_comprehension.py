#!/usr/bin/env python3
'''Module for async comprehension.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using an async comprehending over async_generator and returns them.

    Returns:
    List[float]: A list of 10 random numbers.
    '''
    return [num async for num in async_generator()]
