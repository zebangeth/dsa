class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            raise ValueError("number of piles can not exceed h")
        
        start, end = 1, max(piles)
        while start + 1 < end:
            mid = (start + end) // 2
            if self._hours_needed(piles, mid) > h:
                start = mid
            elif self._hours_needed(piles, mid) < h:
                end = mid
            else:
                end = mid
        
        if self._hours_needed(piles, start) <= h:
            return start
        return end

    def _hours_needed(self, piles, speed):
        hour = 0
        for pile in piles:
            hour += math.ceil(pile / speed)
        return hour