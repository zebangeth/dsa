class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # state: dp[i] is min cost to reach floor i
        # dp = [0] * (len(cost) + 1)

        # # init
        # dp[0], dp[1] = 0, 0

        # # function
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        # return dp[len(cost)]

        prev_2, prev1 = 0, 0
        min_cost = 0
        for i in range(2, len(cost) + 1):
            min_cost = min(cost[i - 1] + prev1, cost[i - 2] + prev_2)
            prev_2, prev1 = prev1, min_cost
        return min_cost