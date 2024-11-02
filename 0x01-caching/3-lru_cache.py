#1/usr/bin/python3
""" LRU cache """

from base_caching import BaseCaching
from collections import deque

class LRUCache(BaseCaching):
    """ LRU cache class """
    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Add an item to the cache """
        if key and item:

            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.queue.popleft()
                print( "DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            self.queue.append(key)

        def get(self, key):
            """ Get an item by key """
            return self.cache_data.get(key) if key in self.cache_data else None
