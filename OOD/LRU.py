class LRU():
    def __init__(self, capacity):
        self.__cache = {}
        self.__queue = []
        self.__capacity = capacity

    def add_to_cache(self, key, val):
        if key not in self.__cache.keys():
            self.__cache[key] = val
            if len(self.__queue) == self.__capacity:
                eviction_key = self.__queue.pop(0)
                del self.__cache[eviction_key]
            self.__queue.append(key)
        return True          

    def get_from_cache(self, key):
        if key in self.__cache.keys():
            self.__queue.remove(key)
            self.__queue.append(key)
            return self.__cache[key]
        else:
            return None



if __name__ == '__main__':
    cache = LRU(2)
    cache.add_to_cache('10', 10)
    cache.add_to_cache('20', 20)
    print(cache.get_from_cache('20'))
    print(cache.get_from_cache('10'))
    cache.add_to_cache('30', 30)
    print(cache.get_from_cache('10'))
    print(cache.get_from_cache('20'))
    print(cache.get_from_cache('30'))
