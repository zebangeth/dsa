class Solution:
    def hammingWeight(self, n: int) -> int:
        num_of_ones = 0
        while n: 
            n = n & (n - 1)
            num_of_ones += 1
        return num_of_ones
