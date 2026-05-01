class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        if self.min_heap and self.max_heap:
            m1 = heapq.heappop(self.min_heap)
            m2 = -heapq.heappop(self.max_heap)
            if m1 < m2:
                m1, m2 = m2, m1
            heapq.heappush(self.min_heap, m1)
            heapq.heappush(self.max_heap, -m2)
        if len(self.min_heap) > len(self.max_heap):
            n = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -n)

    def findMedian(self) -> float:
        print(self.min_heap, self.max_heap)
        if len(self.max_heap) == len(self.min_heap) + 1:
            return -self.max_heap[0]
        n1 = self.min_heap[0]
        n2 = -self.max_heap[0]
        return (n1 + n2) / 2
        