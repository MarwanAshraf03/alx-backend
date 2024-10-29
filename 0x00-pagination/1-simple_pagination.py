#!/usr/bin/env python3
"""Module"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function"""
    end = page * page_size
    start = end - page_size
    return (start, end)


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
        """Function"""
        assert (type(page).__name__ == "int") and (page > 0)
        assert (type(page_size).__name__ == "int") and (page_size > 0)
        tup = index_range(page, page_size)
        dataSet = self.dataset()
        return dataSet[tup[0]: tup[1]]
