class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()
        return self.dfs(nums, target, 0, 0, memo)
        
    def dfs(self, nums, target, i, total, memo):
        if (i, total) in memo:
            return memo[(i, total)]

        if i == len(nums):
            if target == total:
                return 1
            return 0
        
        sum_ways = 0

        sum_ways += self.dfs(nums, target, i + 1, total + nums[i], memo)
        sum_ways += self.dfs(nums, target, i + 1, total - nums[i], memo)

        memo[(i, total)] = sum_ways
        return memo[(i, total)]
