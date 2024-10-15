#!/usr/bin/env python3
'''Task module for measuring execution runtime.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times in parallel and measures the total execution time.

    Returns:
    float: The total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
