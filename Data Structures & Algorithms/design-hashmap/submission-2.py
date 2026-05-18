class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.hmap = [ListNode(-1, -1)] * 100
        self.size = 100

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        node = self.hmap[idx]
        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        node = self.hmap[idx]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
        idx = key % self.size
        node = self.hmap[idx]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
                
            
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)