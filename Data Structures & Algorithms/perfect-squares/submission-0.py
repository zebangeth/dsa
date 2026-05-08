class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] stores the least number of perfect sq numbers that sum to i
        dp = [n] * (n + 1)

        # initialization
        dp[0] = 0
        dp[1] = 1

        # function
        for target in range(2, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target < square:
                    break
                dp[target] = min(dp[target], dp[target - square] + 1)
        return dp[n]