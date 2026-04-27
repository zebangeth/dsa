# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 0, n
        while start + 1 < n:
            mid = (start + end) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                end = mid
            elif guess(mid) == 1:
                start = mid
            else:
                raise ValueError("guess() returend unexpected value")
        
        if guess(start) == 0:
            return start
        return end
            