#!/usr/bin/env python3
import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the coroutine wait_random with the given max_delay.

    Parameters:
    max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    asyncio.Task: The created asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

