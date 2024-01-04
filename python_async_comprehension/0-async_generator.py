#!/usr/bin/python3
""" generator """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random floating-point numbers between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.

    This coroutine will loop 10 times, each time asynchronously waits for
    1 second, and then yields a random number between 0 and 10 using the
    random module.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
