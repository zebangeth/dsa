class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1
        
        start, end = max(nums), sum(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.splits(nums, mid) <= k:
                end = mid
            else:
                start = mid
        
        if self.splits(nums, start) <= k:
            return start
        return end

    def splits(self, nums, size):
        k = 1
        size_remain = size
        for num in nums:
            if size_remain < num:
                size_remain = size
                k += 1
            size_remain -= num
        return k

        