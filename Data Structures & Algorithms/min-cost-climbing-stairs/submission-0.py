class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # state: dp[i] is min cost to reach floor i
        dp = [0] * (len(cost) + 1)

        # init
        dp[0], dp[1] = 0, 0

        # function
        for i in range(2, len(cost) + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        return dp[len(cost)]