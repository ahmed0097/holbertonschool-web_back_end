#!/usr/bin/env python3
""" Create a measure_time function with integers n
and max_delay as arguments that measures the total
execution time """

import time
from typing import List
import random
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """returns total_time / n. Your function should return a float."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return (total_time / 2)
