# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(-1, head)
        prev, slow, fast = dummy, head, head
        while fast:
            for _ in range(k - 1):
                fast = fast.next
                if not fast:
                    break
            if not fast:
                break
            next_start = fast.next
            rev_head, rev_tail = self.reverse(slow, fast)
            prev.next = rev_head
            rev_tail.next = next_start
            prev, slow, fast = rev_tail, next_start, next_start
        return dummy.next

    # return the head and tail for the reversed list
    def reverse(self, head, end):
        prev, curr = None, head
        while prev != end:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev, head
