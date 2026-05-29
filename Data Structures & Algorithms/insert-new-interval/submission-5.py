class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Start with the incoming new interval bounds.
        # These may expand as we detect overlaps with existing intervals.
        n_start, n_end = newInterval

        # Collect all intervals that do not overlap with the new interval.
        # The remaining intervals will stay sorted because the input is sorted.
        result = []

        for (start, end) in intervals:
            # Check whether the current interval overlaps the new interval.
            # If it does, expand the new interval to cover both ranges.
            if end >= n_start and start <= n_end:
                n_start = min(n_start, start)
                n_end = max(n_end, end)
            else:
                # No overlap, so keep the interval as-is.
                result.append([start, end])

        # Insert the merged interval into the correct sorted position.
        # The original code started this loop at 1, which could skip inserting
        # before the first interval and produce incorrect results.
        for i in range(len(result)):
            if result[i][0] > n_end:
                return result[:i] + [[n_start, n_end]] + result[i:]

        # If the merged interval belongs at the end, append it there.
        return result + [[n_start, n_end]]


# Summary of fixes:
# - Fixed the overlap detection so all overlapping intervals are merged correctly,
#   not just intervals containing the start or end of the new interval.
# - Fixed the insertion logic by checking from index 0 instead of 1, which
#   prevents skipping insertion before the first interval.
# - Kept the original variable names and overall structure, while adding comments
#   to clarify each step of the algorithm.