class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.dfs(sorted(nums), 0, [])
        return self.subsets
    
    def dfs(self, nums, start, subset):
        self.subsets.append(subset)
        
        for i in range(start, len(nums)):
            if i - 1 >= 0 and nums[i-1] == nums[i] and i > start:
                continue
            self.dfs(nums, i + 1, subset + [nums[i]])