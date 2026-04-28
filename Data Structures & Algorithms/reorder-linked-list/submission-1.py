# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        mid_node = self._find_mid(head)
        p1 = head
        p2 = mid_node.next
        mid_node.next = None   # 关键：断开前后两段

        p2 = self._reverse(p2)

        dummy = ListNode(-1)
        cur = dummy
        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next
            cur.next = p1
            p1.next = p2
            cur = p2
            p1, p2 = tmp1, tmp2
        if p1:
            cur.next = p1

    # 这个写法会让 slow 停在前半段尾部
    def _find_mid(self, head):
        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def _reverse(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            cur, pre = tmp, cur
        return pre
