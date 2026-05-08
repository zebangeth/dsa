class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # state: dp[i][j] stores the min path sum to grid[i][j]
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        # initialization
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        
        # function
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        
        return dp[len(grid) - 1][len(grid[0]) - 1]

