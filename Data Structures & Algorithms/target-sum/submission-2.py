class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total - target) % 2 != 0:
            return 0
        target_sum = (total - target) // 2

        # state: dp[i][w] stores the no. of ways to get w with nums[:i]
        dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # init
        dp[0][0] = 1

        # state transition
        for i in range(1, len(nums) + 1):
            for w in range(target_sum + 1):
                dp[i][w] = dp[i - 1][w]
                if w - nums[i - 1] >= 0:
                    dp[i][w] += dp[i - 1][w - nums[i - 1]]

        return dp[len(nums)][target_sum]
