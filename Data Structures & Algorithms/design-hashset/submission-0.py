class ListNode:
    def __init__(self, key: int, next=None):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.mset = [None] * self.size


    def add(self, key: int) -> None:
        mkey = key % self.size
        curr_node = self.mset[mkey]
        if not curr_node:
            self.mset[mkey] = ListNode(key)
            return
        while curr_node:
            if curr_node.key == key:
                return
            if not curr_node.next:
                break
        curr_node.next = ListNode(key)

    def remove(self, key: int) -> None:
        mkey = key % self.size
        curr_node = self.mset[mkey]
        dummy_node = ListNode(-1, curr_node)
        prev_node = dummy_node
        while curr_node:
            if curr_node.key == key:
                prev_node.next = curr_node.next
                self.mset[mkey] = dummy_node.next
                return
            curr_node = curr_node.next
            prev_node = prev_node.next

    def contains(self, key: int) -> bool:
        mkey = key % self.size
        curr_node = self.mset[mkey]
        while curr_node:
            if curr_node.key == key:
                return True
            curr_node = curr_node.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)