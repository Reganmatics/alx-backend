#!/usr/bin/env python3
"""Task 1. FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First In First Out cache queue"""
    def __int__(self):
        """constructor from BaseCaching"""
        super().__init__()

    def put(self, key, item):
        """assign to self.cache_data item for the key <key>"""
        if (key is None) or (item is None):
            pass
        else:
            if key in self.cache_data.keys():
                self.cache_data.update({key: item})
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                self.cache_data[key] = item
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """return value for specified key"""
        if (key is None) or (key not in self.cache_data):
            return None
        else:
            return self.cache_data[key]
