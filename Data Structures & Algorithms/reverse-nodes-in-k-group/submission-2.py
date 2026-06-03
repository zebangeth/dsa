# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1, head)
        prv_tail, cur_tail = dummy, head
        while cur_tail:
            # get cur_tail to the tail of the group to be reversed
            for _ in range(k - 1):
                cur_tail = cur_tail.next
                if not cur_tail:
                    return dummy.next
            
            cur_head = prv_tail.next
            next_head = cur_tail.next
            
            # cut current group
            cur_tail.next = None

            # reverse current group
            prv_tail.next = self.reverse(cur_head)

            # reconnect reversed group
            prv_tail = cur_head
            cur_tail = next_head

            prv_tail.next = next_head
        return dummy.next
                
    
    def reverse(self, head):
        prv, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prv
            prv, cur = cur, tmp
        return prv

