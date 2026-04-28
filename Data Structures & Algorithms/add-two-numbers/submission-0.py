# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        
        while p1 or p2:
            if p1 and p2:
                cur_sum = p1.val + p2.val + carry
                p1, p2 = p1.next, p2.next
            elif p1:
                cur_sum = p1.val + carry
                p1 = p1.next
            else:
                cur_sum = p2.val + carry
                p2 = p2.next
            cur.next = ListNode(cur_sum % 10)
            carry = 0
            if cur_sum >= 10:
                carry = 1
            cur = cur.next
        
        if carry:
            cur.next = ListNode(1)
        
        return dummy.next

        

