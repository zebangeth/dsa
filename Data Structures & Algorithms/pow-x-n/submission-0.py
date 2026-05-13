class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            return self.help(x, n, [])
        if n < 0:
            return self.help(1/x, -n, [])
    
    def help(self, x, n, remain):
        if n == 1:
            return x * math.prod(remain)
        return self.help(x * x, n // 2, remain + [x] * (n % 2))
