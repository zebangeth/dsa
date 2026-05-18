class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s, f = 0, 0
        while f < len(nums):
            while f < len(nums) and nums[s] == nums[f]:
                f += 1
            s += 1
            if f < len(nums):
                nums[s] = nums[f]
        return s
