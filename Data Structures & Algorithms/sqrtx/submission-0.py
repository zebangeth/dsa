class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2
            mid_sqr = mid * mid
            if mid_sqr < x:
                start = mid
            elif mid_sqr > x:
                end = mid
            else:
                return mid
        
        if end * end <= x:
            return end
        return start