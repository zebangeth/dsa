# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        before = dummy
        for _ in range(left - 1):
            before = before.next
        
        after = dummy
        for _ in range(right):
            after = after.next
        before_after = after
        after = after.next
        before_after.next = None
        to_reverse = before.next
        before.next = None
        r_head, r_tail = self.reverse(to_reverse)
        before.next = r_head
        r_tail.next = after
        return dummy.next
        
    # return the head and tail of the reversed linked list
    def reverse(self, node):
        if not node or not node.next:
            return node, node
        dummy = ListNode(-1, node)
        pre, cur = None, node
        while cur:
            tmp = cur.next
            cur.next = pre
            cur, pre = tmp, cur
        return pre, dummy.next