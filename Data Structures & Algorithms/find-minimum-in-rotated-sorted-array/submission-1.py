class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]
