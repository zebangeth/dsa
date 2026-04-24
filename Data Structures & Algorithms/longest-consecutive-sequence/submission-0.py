class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            consecutive = 1
            while num - 1 in num_set:
                num -= 1
                consecutive += 1
            longest = max(longest, consecutive)
        return longest
