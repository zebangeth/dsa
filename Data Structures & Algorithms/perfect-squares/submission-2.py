class Solution:
    def numSquares(self, n: int) -> int:
        # state: state[i] stores the least no. of square numbers that sum to i
        dp = [n] * (n + 1)
        
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            for s in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - s * s] + 1)
        return dp[n]