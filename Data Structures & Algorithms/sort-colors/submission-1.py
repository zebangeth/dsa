class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.partition(nums, 0)
        self.partition(nums, 1)
    
    def partition(self, nums, k):
        """
        partition nums array to 2 parts: ["<=k", ">k"]
        """
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] <= k:
                l += 1
            while l < r and nums[r] > k:
                r -= 1
            # stops at the position where l <= r and nums[l] > k, nums[r] <= k
            # swaps the 2 numbers
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1