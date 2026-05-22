class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.dfs(sorted(nums), [], set())
        return self.permutations

    def dfs(self, nums, permutation, visited):
        if len(permutation) == len(nums):
            self.permutations.append(permutation[:])
            return
        
        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited: 
                continue
            permutation.append(nums[i])
            visited.add(i)
            self.dfs(nums, permutation, visited)
            permutation.pop()
            visited.remove(i)
