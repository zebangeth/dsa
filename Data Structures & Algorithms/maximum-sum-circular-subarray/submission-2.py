class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # dp_max[i] stores the max subarray sum ends with nums[i]
        dp_max = nums[:]
        dp_min = nums[:]

        #function
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i], dp_max[i - 1] + nums[i])
            dp_min[i] = min(dp_min[i], dp_min[i - 1] + nums[i])
        
        total = sum(nums)
        min_subarray_sum = min(dp_min)
        max_subarray_sum = max(dp_max)
        if max_subarray_sum < 0:
            return max_subarray_sum
        return max(max_subarray_sum, total - min_subarray_sum)