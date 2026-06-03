class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.dfs(sorted(nums), [], 0)
        return self.subsets
    
    def dfs(self, nums, subset, start):
        self.subsets.append(subset[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, subset, i + 1)
            subset.pop()
