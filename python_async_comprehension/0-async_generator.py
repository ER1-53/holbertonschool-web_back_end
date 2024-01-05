#!/usr/bin/python3
"""
This module defines an asynchronous generator that yields random
floating-point numbers between 0 and 10 after each asynchronous sleep of
1 second.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously and random
    loop IO
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
