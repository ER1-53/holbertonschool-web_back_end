#!/usr/bin/python3
""" generator  """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ generator """
    for i in range(10):
        await  asyncio.sleep(1)
        yield random.uniform(0, 10)

async def async_comprehension() -> Generator[float, None, None]:
    """ generator """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
