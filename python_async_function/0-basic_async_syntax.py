#!/usr/bin/env python3
""" async coroutine """
import asyncio
import random
import typing


async def wait_random(max_delay: int = 10) -> float:
    """ random module """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
