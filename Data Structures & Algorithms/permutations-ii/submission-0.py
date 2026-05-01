class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.dfs(sorted(nums), set(), [])
        return self.permutations
    
    def dfs(self, nums, visited, permutation):
        if len(visited) == len(nums):
            self.permutations.append(permutation[:])
            return
        
        for i, num in enumerate(nums):
            if i in visited:
                continue
            if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited: 
                continue
            visited.add(i)
            self.dfs(nums, visited, permutation + [num])
            visited.remove(i)
