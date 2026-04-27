class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # find the idx of the smallest num that larger than target
        if not nums:
            return 0

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end

        return len(nums)
