class Solution:
    def climbStairs(self, n: int) -> int:
        # state: dp[i] is the number of ways to climb to i
        dp = [0] * (n + 1)

        # initialization
        dp[0] = 1
        dp[1] = 1

        # function
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
