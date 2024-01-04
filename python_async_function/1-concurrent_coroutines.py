#!/usr/bin/env python3
""" running win """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """delay_n = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)])"""
    list_of_delay = []
    for turn in range(n):
        list_of_delay.append(await wait_random(max_delay))
    return sorted(list_of_delay)
