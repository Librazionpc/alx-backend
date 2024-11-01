#!/usr/bin/python3
""" FIFO cache """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.key = []
        
    def put(self, key, item):
        """ Put an item in the cache """
        if key and item:
            self.cache_data[key] = item
            self.key.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = self.key.pop(0)
                print("DISCARD: {}".format(first))
                del self.cache_data[first]

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key) if key in self.cache_data else None
