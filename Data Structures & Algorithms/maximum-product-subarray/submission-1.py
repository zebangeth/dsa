class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre_max = nums[0]
        pre_min = nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i] * pre_max, nums[i] * pre_min, nums[i])
            cur_min = min(nums[i] * pre_max, nums[i] * pre_min, nums[i])
            max_prod = max(max_prod, cur_max)
            pre_max, pre_min = cur_max, cur_min
        return max_prod
            