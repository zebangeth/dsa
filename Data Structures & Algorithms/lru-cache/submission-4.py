class Node:

    def __init__(self, key, val, prv=None, nxt=None):
        self.key = key
        self.val = val
        self.prv = prv
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.nxt, self.tail.prv = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._update(key, self.cache[key].val)
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._update(key, value)
        else:
            if self.capacity == 0:
                to_pop = self.head.nxt
                self.cache.pop(to_pop.key)
                self.head.nxt = to_pop.nxt
                to_pop.nxt.prv = self.head
                self.capacity += 1
            new_node = Node(key, value)
            last = self.tail.prv
            self.tail.prv.nxt, self.tail.prv = new_node, new_node
            new_node.prv = last
            new_node.nxt = self.tail
            self.cache[key] = new_node

            self.capacity -= 1
            
    def _update(self, key, value):
        node = self.cache[key]
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv
        node.prv = self.tail.prv
        node.nxt = self.tail
        node.prv.nxt, self.tail.prv = node, node
        node.val = value
