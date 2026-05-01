class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.dfs(nums, 0, target, [])
        return self.ans
    
    def dfs(self, nums, start, target, combination):
        if target == 0:
            self.ans.append(combination)
            return

        if target < 0 or start >= len(nums):
            return

        for i in range(start, len(nums)):
            self.dfs(nums, i, target - nums[i], combination + [nums[i]])