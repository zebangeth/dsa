class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: 
            return [[]]
        
        permutations = []
        self.dfs(nums, [], set(), permutations) 
        return permutations

    # 递归的定义：找到所有 permutation 开头的 permutations
    def dfs(self, nums, permutation, visited, permutations):
        if len(visited) == len(nums):
            permutations.append(permutation[:])
            return
        
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            self.dfs(nums, permutation + [num], visited, permutations)
            visited.remove(num)