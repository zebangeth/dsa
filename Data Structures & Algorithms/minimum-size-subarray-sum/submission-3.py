class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        array_len = float('inf')
        array_sum = 0
        while r < len(nums):
            array_sum += nums[r]
            while l <= r and array_sum >= target:
                array_len = min(array_len, r - l + 1)
                array_sum -= nums[l]
                l += 1
            r += 1
        
        return 0 if array_len == float('inf') else array_len
