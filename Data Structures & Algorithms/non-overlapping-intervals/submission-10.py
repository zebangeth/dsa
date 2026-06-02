class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s_intervals = sorted(intervals, key=lambda x: x[1])
        last_end = -float('inf')
        overlap = 0
        for (start, end) in s_intervals:
            if start >= last_end:
                last_end = end
            else:
                overlap += 1
        return overlap
