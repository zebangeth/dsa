class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        help_nums = [1] + nums + [1]
        prefix = [1] * len(help_nums)
        suffix = [1] * len(help_nums)
        for i in range(1, len(help_nums) - 1):
            prefix[i] = prefix[i - 1] * help_nums[i - 1]
        
        for i in range(len(help_nums) - 2, 0, -1):
            suffix[i] = suffix[i + 1] * help_nums[i + 1]
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i + 1] * suffix[i + 1]
        return result
            