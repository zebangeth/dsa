class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = dict()
        return self.dfs(tuple(nums), memo)
        
    def dfs(self, nums, memo):
        if nums in memo:
            return memo[nums]

        if not nums:
            return 0

        max_coins = 0
        for i, num in enumerate(nums):
            pre = 1 if i == 0 else nums[i - 1]
            nxt = 1 if i == len(nums) - 1 else nums[i + 1]
            max_coins = max(
                max_coins,
                pre * nums[i] * nxt + self.dfs(nums[:i] + nums[i+1:], memo)
            )

        memo[nums] = max_coins
        return max_coins