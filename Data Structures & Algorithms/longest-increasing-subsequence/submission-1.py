class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # state: dp[i] stores the longest LIS including nums[i]
        dp = [1] * len(nums)

        # function
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)        
        return max(dp)
