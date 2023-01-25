#!/usr/bin/env python3
"""Task 0. Basic Dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """cache class"""
    def __init__(self):
        """contrsuctor inheriting from BaseCaching"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """assign to the dictionary key, value pairs"""
        if (key is None) or (item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get value linked to <key>"""
        if (key is None) or (key not in self.cache_data):
            return None

        else:
            return self.cache_data[key]
