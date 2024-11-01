#!/usr/bin/python3
"""basic cache class Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """BasicCache Class"""

    def __init__(self):
        """initialization"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """inputs data in the cache dictionary in LIFO order"""
        if not (key and item):
            return
        klist = list(self.cache_data.keys())
        if key in klist:
            del self.cache_data[key]
            self.freq[f"{key}.F"] += 1
            self.cache_data[key] = item
            return

        if (key not in klist) and (len(klist) >= self.MAX_ITEMS):
            self.deleteLFU()
            self.cache_data[key] = item
            self.freq[f"{key}.F"] = 1
            return

        if key not in klist:
            self.cache_data[key] = item
            self.freq[f"{key}.F"] = 1
            return

    def get(self, key):
        """gets data from the cache dictionary"""
        if not key:
            return None
        if key not in self.cache_data.keys():
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        self.freq[f"{key}.F"] += 1
        return self.cache_data[key]

    def deleteLFU(self):
        llist = {k: v for k, v in
                 sorted(self.freq.items(), key=lambda item: item[1])}
        lf = llist[list(llist.keys())[0]]
        llist = [k for k, v in self.freq.items() if v == lf]
        for key in self.cache_data.keys():
            if f"{key}.F" in llist:
                print(f"DISCARD: {key}")
                del self.cache_data[key]
                del self.freq[f"{key}.F"]
                return
