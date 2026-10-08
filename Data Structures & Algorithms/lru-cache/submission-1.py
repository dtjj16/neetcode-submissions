class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_right(self.cache[key])
            return self.cache[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            #update LL
            self.remove(self.cache[key])
            
        #update hashmap, insert new node at right
        self.cache[key] = Node(key, value)
        self.insert_right(self.cache[key]) # <--

        #check size
        if self.capacity < len(self.cache):
            #remove left 
            lru = self.LRU.next
            self.remove(lru)
            del self.cache[lru.key]
        

    def insert_right(self, currNode):
        #involves manipulating pointers from MRU
        leftNode, rightNode = self.MRU.prev, self.MRU
        #insert between left and right
        leftNode.next = currNode
        rightNode.prev = currNode
        currNode.next = rightNode
        currNode.prev = leftNode


    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
