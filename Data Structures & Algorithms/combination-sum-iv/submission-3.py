from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = dict() # key: remain, val: # of combinations
        return self.dfs(memo, nums, target)

    def dfs(self, memo, nums, remain):
        if remain in memo:
            return memo[remain]

        if remain == 0:
            return 1
        
        if remain < 0:
            return 0
        
        count = 0
        for num in nums:
            count += self.dfs(memo, nums, remain - num)
        memo[remain] = count
        return count