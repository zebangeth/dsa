class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s_intervals = sorted(intervals, key=lambda x: x[1])
        overlaps = 0
        prv_end = -float('inf')
        for (start, end) in s_intervals:
            if start < prv_end:
                overlaps += 1
            else:
                prv_end = end
        return overlaps