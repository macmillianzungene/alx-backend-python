#!/usr/bin/env python3
'''Module for async generator.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.
Returns:
    Generator[float, None, None]: A generator yielding random numbers between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
