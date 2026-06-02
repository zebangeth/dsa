class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 1:
            return 0
        min_cost_1, min_cost_2 = 0, 0
        for i in range(2, len(cost) + 1):
            min_cost = min(min_cost_1 + cost[i - 1], min_cost_2 + cost[i - 2])
            min_cost_1, min_cost_2 = min_cost, min_cost_1
        
        return min_cost

# cost = [1, 2, 3]
# min_cost_1 = 0
# min_cost_2 = 0


