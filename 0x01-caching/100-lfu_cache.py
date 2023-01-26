#!/usr/bin/env python3
"""Task 5. LFU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently Used Cache"""

    def __init__(self):
        """LFU Cache constructor"""
        super().__init__()

    def put(self, key, item):
        """LFU Cache Implementation"""
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
                    lfu_key = list(self.cache_data.keys())[0]
                    self.cache_data.pop(lfu_key)
                    self.cache_data.update({key: item})
                    print(f"DISCARD: {key}")

    def get(self, key):
        """return value for associated key"""
        if (key is None) or (key not in self.cache_data.keys()):
            return None
        else:
            return self.cache_data[key]
