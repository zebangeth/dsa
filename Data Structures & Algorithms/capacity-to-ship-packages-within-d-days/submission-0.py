class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if not weights:
            return 0
        
        start, end = max(weights), sum(weights)
        while start + 1 < end:
            mid = (start + end) // 2
            if self._get_days(weights, mid) < days:
                end = mid
            elif self._get_days(weights, mid) > days:
                start = mid
            else:
                end = mid
        
        print(start, end)
        print(self._get_days(weights, start))
        if self._get_days(weights, start) <= days:
            return start
        return end

    def _get_days(self, weights, capacity):
        days = 0
        capacity_remain = capacity
        for weight in weights:
            if capacity_remain < weight:
                capacity_remain = capacity
                days += 1
            capacity_remain -= weight
        return days + 1