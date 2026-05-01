class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        self.dfs(nums, 0, 0)
        return self.ans
    
    def dfs(self, nums, i, cur_xor):
        if i == len(nums):
            self.ans += cur_xor
            return
        
        self.dfs(nums, i + 1, cur_xor)
        self.dfs(nums, i + 1, cur_xor ^ nums[i])
