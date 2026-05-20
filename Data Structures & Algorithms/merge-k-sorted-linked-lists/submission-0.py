# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        heap = [(head.val, id(head), head) for head in lists if head]
        heapq.heapify(heap)

        while heap:
            _, _, head = heapq.heappop(heap)
            if head.next:
                heapq.heappush(heap, (head.next.val, id(head.next), head.next))
            cur.next = head
            head.next = None
            cur = cur.next
        
        return dummy.next
