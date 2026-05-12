class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_intervals = collections.deque(sorted(intervals))
        sorted_queries = sorted([[query, idx] for (idx, query) in enumerate(queries)])

        heap = []
        result = [-1] * len(queries)
        for (query, idx) in sorted_queries:
            # ensure potential answer in the heap
            while sorted_intervals and sorted_intervals[0][0] <= query:
                (l, r) = sorted_intervals.popleft()
                heapq.heappush(heap, (r - l + 1, r))
            
            # pop invalid intervals
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            # record the answer
            if heap:
                result[idx] = heap[0][0]

        return result
            
# sorted_queries = [[1, 2], [2, 0], [3, 1], [6, 4], [7, 3], [8, 5]]
# sorted_intervals = [[1,3],[2,3],[3,7],[6,6]]

# heap = [[3, 3], ]
# result = [-1, -1, -1, -1, -1, -1]
# l = 1
# r = 3

