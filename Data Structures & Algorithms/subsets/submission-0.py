class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.dfs(nums, 0, [])
        return self.subsets
    
    def dfs(self, nums, i, subset):
        if i == len(nums):
            self.subsets.append(subset)
            return
        
        self.dfs(nums, i + 1, subset + [nums[i]])
        self.dfs(nums, i + 1, subset)

