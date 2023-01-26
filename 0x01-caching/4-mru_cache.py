#!/usr/bin/env python3
"""Task 4. MRUCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used cache"""

    def __init__(self):
        """mru cache constructor"""
        super().__init__()

    def put(self, key, item):
        """MRU implementation"""
        if (key is None) or (item is None):
            pass
        else:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data.keys():
                    self.cache_data.update({key: item})
                    print(f"DISCARD: {key}")
                elif key not in self.cache_data.keys():
                    last_key = list(self.cache_data.keys())[-1]
                    self.cache_data.pop(last_key)
                    self.cache_data.update({key: item})
                    print(f"DISCARD: {key}")

    def get(self, key):
        """return value for specified key"""
        if (key is None) or (key not in self.cache_data.keys()):
            return None
        else:
            return self.cache_data[key]
