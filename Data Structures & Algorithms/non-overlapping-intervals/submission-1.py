class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        removed = 0
        prev_end = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            # overlapping
            if sorted_intervals[i][0] < prev_end:
                removed += 1
            else:
                prev_end = sorted_intervals[i][1]
        
        return removed
