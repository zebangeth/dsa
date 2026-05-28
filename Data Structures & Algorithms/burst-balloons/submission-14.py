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
            # i 作为 (l, r) 之间 最后一个被戳爆的气球
            # i 左右的气球都被戳完
            left = self.dfs(nums, l, i, memo)
            right = self.dfs(nums, i, r, memo)
            # 最后戳 i 的时候 i 的左右是 l 和 r
            gain = nums[l] * nums[i] * nums[r]

            max_coins = max(max_coins, left + right + gain)
        memo[(l, r)] = max_coins
        return max_coins

