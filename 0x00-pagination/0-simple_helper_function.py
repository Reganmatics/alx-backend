#!/usr/bin/env python3
"""
Task 0. Simple helper funtion
"""


def index_range(page, page_size) -> tuple:
    """
    args:
        page -> int
        page_size -> int

    return -> tuple of size 2
    """
    '''
    start = page * 10
    end = start + 15
    '''
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size
    return tuple((start, end))
