class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
        result = []
        for (start, end) in intervals:
            if end >= n_start and start <= n_end:
                n_start = min(n_start, start)
                n_end = max(n_end, end)
            else:
                result.append([start, end])
        

        for i in range(len(result)):
            if result[i][0] > n_end:
                return result[:i] + [[n_start, n_end]] + result[i:]

        return result + [[n_start, n_end]]
            
