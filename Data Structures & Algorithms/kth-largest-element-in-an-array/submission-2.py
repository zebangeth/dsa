class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)
        
    def quick_select(self, nums, l, r, k):
        pivot = nums[(l + r) // 2]

        o_l, o_r = l, r
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        if k >= l:
            return self.quick_select(nums, l, o_r, k)
        elif k <= r:
            return self.quick_select(nums, o_l, r, k)
        else:
            return nums[k]