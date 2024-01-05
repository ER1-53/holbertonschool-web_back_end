#!/usr/bin/env python3
"""
Import async_comprehension from the
previous file and write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather
"""
import random
from typing import Generator
import asyncio
import time


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


async def measure_runtime() -> Generator[float, None, None]:
    """
    loop to 10 time
    """
    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time
    return total_time
