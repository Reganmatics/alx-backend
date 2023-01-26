#!/usr/bin/env python3
"""Task 2. LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Last In First Out cache"""

    def __int__(self):
        """class constructor"""
        super().__init__()

    def put(self, key, item):
        """lifo implementation"""
        if (key is None) or (item is None):
            return None
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data.keys():
                    self.cache_data.update({key: item})
                    print(f"DISCARD: {key}")
                else:
                    last_key = list(self.cache_data.keys())[-1]
                    self.cache_data.pop(last_key)
                    self.cache_data.update({key: item})
                    print(f"DISCARD: {last_key}")

    def get(self, key):
        """return value for specified key"""
        return self.cache_data[key]
