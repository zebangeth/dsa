class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-w for w in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            w1 = -heapq.heappop(heap)
            w2 = -heapq.heappop(heap)
            heapq.heappush(heap, -abs(w1 - w2))
        return -heap[0]