class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = dict()
        return self.dfs([1] + nums + [1], 0, len(nums)+1, memo)

    # in this interval which one is the last to pop    
    def dfs(self, nums, l, r, memo):
        if l + 1 == r:
            return 0
        
        if (l, r) in memo:
            return memo[(l, r)]
        
        max_coins = 0
        for i in range(l + 1, r):
            max_coins = max(
                max_coins, 
                sum([
                    self.dfs(nums, l, i, memo),
                    self.dfs(nums, i, r, memo),
                    nums[l] * nums[i] * nums[r]
                ])
            )
        memo[(l, r)] = max_coins
        return max_coins

