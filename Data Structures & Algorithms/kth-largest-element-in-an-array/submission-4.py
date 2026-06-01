class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            raise ValueError("invalid k")
        return self.helper(nums, len(nums) - k, 0, len(nums) - 1)

    def helper(self, nums, k, start, end):
        pivot = nums[start]
        l, r = start, end
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        if k <= r:
            return self.helper(nums, k, start, r)
        elif k >= l:
            return self.helper(nums, k, l, end)
        else:
            return nums[k]

                