class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals)
        result = [sorted_intervals[0]]

        i = 1
        while i < len(sorted_intervals):
            # overlapping
            if sorted_intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], sorted_intervals[i][1])
                result[-1][0] = min(result[-1][0], sorted_intervals[i][0])
            else:
                result.append(sorted_intervals[i])
            i += 1
        return result
