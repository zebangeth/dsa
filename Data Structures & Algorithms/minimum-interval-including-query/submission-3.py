class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        s_queries = sorted([(q, i) for i, q in enumerate(queries)])
        s_intervals = collections.deque(sorted(intervals))
        heap = []
        result = [-1] * len(queries)
        for q, i in s_queries:
            while s_intervals and q >= s_intervals[0][0]:
                interval = s_intervals.popleft()
                heapq.heappush(heap, (interval[1] - interval[0] + 1, interval))
            while heap and heap[0][1][1] < q:
                heapq.heappop(heap)
            if heap:
                result[i] = heap[0][0]
        return result


            



