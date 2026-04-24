class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = nums
        heapq.heapify(heap)
        result = []
        while heap:
            nxt = heapq.heappop(heap)
            result.append(nxt)
        return result
        