class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        sorted_intervals = collections.deque(sorted(intervals))
        heap = []
        result = [-1] * len(queries)
        for (q, i) in sorted_queries:
            while sorted_intervals and sorted_intervals[0][0] <= q:
                interval = sorted_intervals.popleft()
                heapq.heappush(heap, (interval[1] - interval[0] + 1, interval))
            min_interval = -1
            while min_interval == -1 and heap:
                size, interval = heap[0]
                if interval[1] < q:
                    heapq.heappop(heap)
                    continue
                min_interval = size
            result[i] = min_interval
        return result
