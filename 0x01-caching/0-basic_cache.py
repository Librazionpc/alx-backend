#!/usr/bin/python3
"""0-basic_cache.py"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""
    def put(self, key, item):
        """Put an item in the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key) if key in self.cache_data else None
