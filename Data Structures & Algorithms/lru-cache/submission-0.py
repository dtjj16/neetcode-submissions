# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = [] # store the most frquently used elements in this list
        #LRU and the left, MRU on the right
        self.capacity = capacity

    def get(self, key: int) -> int:
        for k, v in self.cache:
            if k == key:
                self.cache.remove((k,v))
                self.cache.append((k,v))
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        found = False
        for k,v in self.cache:
            if k == key:
                found = True
                self.cache.remove((k,v))
                self.cache.append((key,value))
                break
    
        if not found:
            curr_size = len(self.cache)
            if curr_size == self.capacity:
                self.cache = self.cache[1:]
            self.cache.append((key,value))
        

        
        
     











# lets implement it naively 