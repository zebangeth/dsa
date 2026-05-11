class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # max_sub, cur_sub = nums[0], 0
        # for num in nums:
        #     if cur_sub < 0:
        #         cur_sub = 0
        #     cur_sub += num
        #     max_sub = max(max_sub, cur_sub)
        # return max_sub

        # state: dp[i] stores the max subarray sum that ends with nums[i]
        dp = nums[:]

        # function
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], dp[i])
        return max(dp)

