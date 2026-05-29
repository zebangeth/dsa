class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
        result = []
        for (start, end) in intervals:
            if end >= n_start and start <= n_end:
                n_start = min(n_start, start)
                n_end = max(n_end, end)
            elif n_end < start:
                result.append([n_start, n_end])
                n_start, n_end = start, end
            elif n_start > end:
                result.append([start, end])
                

        # for i in range(len(result)):
        #     if result[i][0] > n_end:
        #         return result[:i] + [[n_start, n_end]] + result[i:]
        if not result or n_start > result[-1][1]:
            return result + [[n_start, n_end]]
        return result
            
