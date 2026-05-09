class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict() # remain, i
        return self.dfs(memo, nums, 0, target)
        
    
    def dfs(self, memo, nums, i, remain):
        if (remain, i) in memo:
            return memo[(remain, i)]

        if i == len(nums) and remain == 0:
            return 1
        if i == len(nums):
            return 0

        count = 0
        # option 1: add
        count += self.dfs(memo, nums, i + 1, remain - nums[i])
        # option 2: substract
        count += self.dfs(memo, nums, i + 1, remain + nums[i])

        memo[(remain, i)] = count
        return count

