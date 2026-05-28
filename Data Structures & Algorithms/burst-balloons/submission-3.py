class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)

        # dp[l][r]: max coins from bursting balloons strictly between l and r
        dp = [[0] * n for _ in range(n)]

        # length is the distance between l and r
        # length = 2 means there is exactly one balloon between l and r
        for length in range(2, n):
            for l in range(0, n - length):
                r = l + length

                # choose the last balloon to burst between l and r
                for i in range(l + 1, r):
                    dp[l][r] = max(
                        dp[l][r],
                        dp[l][i] + dp[i][r] + balloons[l] * balloons[i] * balloons[r]
                    )

        return dp[0][n - 1]
