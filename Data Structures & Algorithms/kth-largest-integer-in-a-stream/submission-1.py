class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if len(nums) < k - 1:
            raise ValueError('must have >= k - 1 elements in nums when initialize')
        self.heap = list(nums)
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
