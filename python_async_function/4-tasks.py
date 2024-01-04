#!/usr/bin/env python3
""" return task """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task delay"""
    list_of_delay = []
    for turn in range(n):
        list_of_delay.append(
            await asyncio.create_task(task_wait_random(max_delay)))
    return sorted(list_of_delay)
task_wait_n
