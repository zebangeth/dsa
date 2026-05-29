class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s_intervals = sorted(intervals)
        overlaps = 0
        prv_end = -float('inf')
        for (start, end) in s_intervals:
            if start < prv_end:
                overlaps += 1
                prv_end = min(end, prv_end)
            else:
                prv_end = end
        return overlaps