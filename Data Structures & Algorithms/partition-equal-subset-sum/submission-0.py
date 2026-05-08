class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = sum(nums) // 2

        # state: dp[i][w] stores if possible to use nums[:i] to get total w
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        # initialization
        for i in range(len(nums) + 1):
            dp[i][0] = True

        # initialization
        for i in range(1, len(nums) + 1):
            for w in range(target + 1):
                if nums[i - 1] > target:
                    return False
                if nums[i - 1] > w:
                    continue
                dp[i][w] = dp[i - 1][w] or dp[i - 1][w - nums[i - 1]]


        return dp[len(nums)][target]