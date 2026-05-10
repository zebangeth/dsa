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
        for i in range(len(nums)):
            pre = 1 if i == 0 else nums[i - 1]
            nxt = 1 if i == len(nums) - 1 else nums[i + 1]
            max_coins = max(
                max_coins, 
                self.dfs(tuple(nums[:i] + nums[i+1:]), memo) + pre * nxt * nums[i]
            )
        memo[nums] = max_coins
        return max_coins