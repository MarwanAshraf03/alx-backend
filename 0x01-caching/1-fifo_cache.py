#!/usr/bin/python3
"""basic cache class Module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """BasicCache Class"""

    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """inputs data in the cache dictionary in FIFO order"""
        if not (key and item):
            return
        klist = list(self.cache_data.keys())
        if (key not in klist)\
            and\
                (len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS):
            print(f"DISCARD: {klist[0]}")
            del self.cache_data[klist[0]]
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """gets data from the cache dictionary"""
        if not key:
            return None
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
