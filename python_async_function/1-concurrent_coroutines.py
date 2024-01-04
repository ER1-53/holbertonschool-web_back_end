#!/usr/bin/env python3
import asyncio
from typing import List
""" running win """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Perform asynchronous waiting using wait_random.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay value for each wait_random call.

    Returns:
        typing.List[float]: List of delays in ascending order.

    Note:
        This function uses asyncio.gather to concurrently run wait_random n
        times.
        The list of delays is returned in ascending order without using sort()
        due to concurrency.
    """
    
    list_of_delay = []
    for turn in range(n):
        list_of_delay.append(await wait_random(max_delay))
    return sorted(list_of_delay)
