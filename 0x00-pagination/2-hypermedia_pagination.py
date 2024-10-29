#!/usr/bin/env python3
"""Module"""
from typing import Tuple, List, Mapping, Any, Dict, Union
import csv
import math


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List]]:
        """Function"""
        data = self.get_page(page, page_size)
        dataSet = self.dataset()
        next_page = page + 1 if len(data) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(dataSet)/page_size)
        ret = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return ret
