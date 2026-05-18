class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
            
        for num in nums:
            if 0 < abs(num) <= len(nums):
                if nums[abs(num) - 1] == 0:
                    nums[abs(num) - 1] = -1
                else:
                    nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1