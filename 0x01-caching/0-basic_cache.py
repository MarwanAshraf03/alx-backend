#!/usr/bin/python3
"""basic cache class Module"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""

    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """inputs data in the cache dictionary"""
        if not (key and item):
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets data from the cache dictionary"""
        if not key:
            return None
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
