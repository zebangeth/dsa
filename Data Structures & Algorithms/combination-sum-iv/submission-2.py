from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = tuple(nums)

        @lru_cache(None)
        def dfs(cur_sum):
            if cur_sum == target:
                return 1
            
            if cur_sum > target:
                return 0
            
            count = 0
            for num in nums:
                count += dfs(cur_sum + num)
            
            return count
        
        return dfs(0)