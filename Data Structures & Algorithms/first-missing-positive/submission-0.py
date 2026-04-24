class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        min_num = 0
        while min_num + 1 in unique:
            min_num += 1
        return min_num + 1