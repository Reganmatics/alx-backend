#!/usr/bin/env python3
"""
Task 2. Hypermedia Pagination
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
    start = page * 10
    end = start + 15
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

    def get_hyper(self, page: int, page_size: int):
        """get hypermedia
        """
        assert (type(page) == int and type(page_size) == int) and \
               (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        data = self.dataset()
        get_page = self.get_page(page, page_size)
        if page > 1 and page < len(data):
            return {"page_size": page_size,
                    "page": page,
                    "data": get_page,
                    "next_page": page + 1,
                    "prev_page": page - 1,
                    "total_pages": len(data)}
        elif page == 1:
            return {"page_size": page_size,
                    "page": page,
                    "data": get_page,
                    "next_page": page + 1,
                    "prev_page": None,
                    "total_pages": len(data)}
        elif page == len(data):
            return {"page_size": page_size,
                    "page": page,
                    "data": get_page,
                    "next_page": None,
                    "prev_page": page - 1,
                    "total_pages": len(data)}
