# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        if not head or not head.next:
            return head
        
        node = head
        while node.next:
            temp = node.next
            node.next = ListNode(gcd(node.val, temp.val), temp)
            node = temp
        
        return head