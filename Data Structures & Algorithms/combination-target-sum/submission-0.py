class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.dfs(nums, 0, target, [])
        return self.ans
    
    def dfs(self, nums, i, target, combination):
        if target == 0:
            self.ans.append(combination)
            return

        if target < 0 or i >= len(nums):
            return

        # 选 nums[i]，因为可以重复使用，所以 i 不变
        self.dfs(nums, i, target - nums[i], combination + [nums[i]])

        # 不选 nums[i]，看下一个数
        self.dfs(nums, i + 1, target, combination)