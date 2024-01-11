#!/usr/bin/env python3
"""
function named index_range that takes
two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index all page
    """
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
