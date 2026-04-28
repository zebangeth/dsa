# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        return prev

        # if not head or not head.next:
        #     return head
        
        # reversed_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        
        # return reversed_head
