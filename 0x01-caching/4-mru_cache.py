#!/usr/bin/python3
"""basic cache class Module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """BasicCache Class"""

    def __init__(self):
        """initialization"""
        super().__init__()

    def put(self, key, item):
        """inputs data in the cache dictionary in LIFO order"""
        if not (key and item):
            return
        klist = list(self.cache_data.keys())
        if key in klist:
            del self.cache_data[key]
        if (key not in klist) and (len(klist) >= self.MAX_ITEMS):
            print(f"DISCARD: {klist[-1]}")
            del self.cache_data[klist[-1]]
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item

    def get(self, key):
        """gets data from the cache dictionary"""
        if not key:
            return None
        if key not in self.cache_data.keys():
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return self.cache_data[key]
