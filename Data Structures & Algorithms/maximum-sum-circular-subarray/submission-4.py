class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_prefix = 0
        max_prefix, min_prefix = 0, 0
        max_sub, min_sub = -float('inf'), float('inf')
        for i in range(len(nums)):
            cur_prefix += nums[i]
            max_prefix = max(max_prefix, cur_prefix)
            min_prefix = min(min_prefix, cur_prefix)
            max_sub = max(max_sub, cur_prefix - min_prefix)
            min_sub = min(min_sub, cur_prefix - max_prefix)
        if all([num < 0 for num in nums]):
            return max(nums)
        return max(max_sub, sum(nums) - min_sub)