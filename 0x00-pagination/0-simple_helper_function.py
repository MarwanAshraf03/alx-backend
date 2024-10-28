#!/usr/bin/env python3
"""Module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function"""
    end = page * page_size
    start = end - page_size
    return (start, end)
