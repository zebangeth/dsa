class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.pow(1 / x, -n)
        return self.pow(x, n)
    
    def pow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 1:
            return self.pow(x * x, n // 2) * x
        return self.pow(x * x, n // 2)