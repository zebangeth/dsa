class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 1
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            first = num
            last = num + 1
            while last in nums_set:
                longest = max(longest, last - first + 1)
                last += 1
        return longest
