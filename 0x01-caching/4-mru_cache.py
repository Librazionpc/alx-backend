#1/usr/bin/python3
""" MRU cache """

from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """ mRU cache class """
    def __init__(self):
        super().__init__()
        self.stack = deque()

    def put(self, key, item):
        """ Add an item to the cache """
        if key and item:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.stack.pop()
                print( "DISCARD: {}".format(mru_key))
                del self.cache_data[mru_key]

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key) if key in self.cache_data else None
