#!/usr/bin/python3
""" LIFO cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache class """
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
                last = self.key.pop(-2)
                print("DISCARD: {}".format(last))
                del self.cache_data[last]

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key) if key in self.cache_data else None
