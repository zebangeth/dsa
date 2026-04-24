class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        min_num = 1
        while min_num in unique:
            min_num += 1
        return min_num