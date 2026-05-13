class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            ints = [int(i) for i in str(n)]
            res = 0
            for i in ints:
                res += i * i
            if res in seen:
                return False
            seen.add(res)
            n = res
        return True