# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode(-1, head)

        # cut the original linked list into m lists of length k
        list_heads, no_reverse_head = self.cut(head, k)

        last_tail = dummy
        # reverse each of the linked list and connect
        for head in list_heads:
            r_head, r_tail = self.reverse(head)
            last_tail.next = r_head
            last_tail = r_tail
        last_tail.next = no_reverse_head
        
        return dummy.next

        
    def cut(self, head, k):
        list_heads = [head]
        cur = head
        cur_len = 1
        while cur:
            cur = cur.next
            cur_len += 1
            if cur_len == k and cur:
                nxt_head = cur.next
                cur.next = None
                list_heads.append(nxt_head)
                cur = nxt_head
                cur_len = 1
        
        # count last list len
        last_head = list_heads[-1]
        cur = last_head
        last_len = 0
        while cur:
            cur = cur.next
            last_len += 1
        no_reverse_head = None
        if last_len < k:
            no_reverse_head = last_head
            list_heads = list_heads[:-1]
        return list_heads, no_reverse_head

        
    def reverse(self, head):
        r_tail = head
        prv, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prv
            prv, cur = cur, tmp
        return prv, r_tail

