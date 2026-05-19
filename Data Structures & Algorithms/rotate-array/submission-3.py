class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.flip(nums, 0, len(nums) - 1)
        self.flip(nums, 0, k - 1)
        self.flip(nums, k, len(nums) - 1)

        
    def flip(self, nums, start, end):
        l, r = start, end
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
