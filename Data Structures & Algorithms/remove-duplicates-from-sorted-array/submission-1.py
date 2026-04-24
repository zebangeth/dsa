class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow: the next place
        slow, fast = 0, 0
        while fast < len(nums):
            nums[slow] = nums[fast]
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1
            slow += 1
        return slow
