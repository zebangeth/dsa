class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # rotating an array by k is equivalent to moving the last k elements to the front
        # 1. reverse the entire array. Now the last k elements are at the front
        # 2. reverse the first k elements to fix their order
        # 2. reverse the remaining elements to restore their original order
        n = len(nums)
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k % n - 1)
        self.reverse(nums, k % n, n - 1)
        
    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1