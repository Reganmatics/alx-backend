#!/usr/bin/env python3
"""
Task 1. simple Pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return a paginated dataset
        """
        assert (type(page) == int and type(page_size) == int) and \
               (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        data = self.dataset()
        try:
            return [data[i] for i in range(start, end)]
        except IndexError:
            return []
