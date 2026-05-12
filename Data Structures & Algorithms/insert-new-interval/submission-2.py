class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        new_start, new_end = newInterval
        for i, (start, end) in enumerate(intervals):
            # no overlap
            if end < new_start:
                new_intervals.append([start, end])
            elif new_end < start:
                new_intervals.append([new_start, new_end])
                return new_intervals + intervals[i:]
            elif start <= new_start <= end or start <= new_end <= end:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        
        if not new_intervals or new_intervals[-1][1] < new_start:
            new_intervals.append([new_start, new_end])
        
        return new_intervals
