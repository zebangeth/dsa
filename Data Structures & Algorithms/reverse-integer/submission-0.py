class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        while x != 0:
            res = 10 * res + x % 10
            if res < -(1<<31) or res > (1<<31) - 1:
                return 0
            x //= 10
        return res * sign
