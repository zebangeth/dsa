# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) <= 2:
#             return max(nums)

#         # state: dp[i] stores the max can rob from nums[:i + 1] if rob nums[i]
#         dp = [0] * (len(nums) + 1)

#         # init:
#         dp[0] = nums[0]
#         dp[1] = nums[1]
#         dp[2] = nums[0] + nums[2]

#         # function
#         for i in range(3, len(nums)):
#             dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
#         return max(dp[len(nums) - 1], dp[len(nums) - 2])


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]