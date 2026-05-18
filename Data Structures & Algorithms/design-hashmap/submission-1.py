class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.hmap = [None] * 100
        self.size = 100

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        node = self.hmap[idx]
        dummy = ListNode(-1, -1, node)
        cur = dummy
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
        self.hmap[idx] = dummy.next
        

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
        dummy = ListNode(-1, -1, node)
        cur = dummy
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.hmap[idx] = dummy.next
                return
            cur = cur.next
                
            
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)