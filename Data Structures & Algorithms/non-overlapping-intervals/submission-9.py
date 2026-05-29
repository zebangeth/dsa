class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        s_intervals = sorted(intervals, key=lambda x: x[1])
        overlaps = 0
        prv_end = -float('inf')
        for (start, end) in s_intervals:
            if start < prv_end:
                # overlap: remove the later ended one, so prv_end no update
                overlaps += 1
            else:
                # no overlap
                prv_end = end
        return overlaps