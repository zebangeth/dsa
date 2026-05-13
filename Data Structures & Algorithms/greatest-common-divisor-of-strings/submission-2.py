class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(x: int, y: int) -> int: # Greatest Common Divisor
            if x < y:
                x, y = y, x
            while y != 0:
                x, y = y, x % y
            return x
        
        max_len = gcd(len(str1), len(str2))
        for i in range(max_len, 0, -1):
            if not (len(str1) % i == 0 and len(str2) % i == 0):
                continue
            if str1[:i] * (len(str1) // i) == str1 and str1[:i] * (len(str2) // i) == str2:
                return str1[:i]
        
        return ""