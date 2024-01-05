#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loop to 10 time
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> Generator[float, None, None]:
    """
    check a random number
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
