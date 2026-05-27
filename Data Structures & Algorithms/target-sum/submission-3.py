class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.res = 0
        self.dfs(nums, 0, target, 0)
        return self.res
        
    def dfs(self, nums, i, target, total):
        if i == len(nums):
            if target == total:
                self.res += 1
            return
        
        self.dfs(nums, i + 1, target, total + nums[i])
        self.dfs(nums, i + 1, target, total - nums[i])
