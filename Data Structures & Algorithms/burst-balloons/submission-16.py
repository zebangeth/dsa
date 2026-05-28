class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        points = [1] + nums + [1]
        n = len(points)

        # state: dp stores the max coins you can collect from i+1th to j-1th ballons
        dp = [[0] * (n) for _ in range(n)]

        # function
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i][k] + points[i] * points[k] * points[j] + dp[k][j]
                    )

        return dp[0][n - 1]