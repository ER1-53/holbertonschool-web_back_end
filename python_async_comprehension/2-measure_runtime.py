#!/usr/bin/python3
""" generator  """
import random
from typing import Generator
import asyncio
import time


async def async_generator() -> Generator[float, None, None]:
    """ generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> Generator[float, None, None]:
    """ generator """
    random_numbers = [number async for number in async_generator()]
    return random_numbers


async def measure_runtime() -> Generator[float, None, None]:
    """ generator """
    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    total_time = end_time - start_time
    return total_time
