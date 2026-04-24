class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Solution 1: using a set to store unique values
        # and then check if num exist starting from 1
        # O(n), O(n)
        # ---
        # unique = set(nums)
        # min_num = 1
        # while min_num in unique:
        #     min_num += 1
        # return min_num

        # Solution 2: using the nums array as the hashset
        # nums[idx] can represent if num=idx in nums
        # how to store? by the sign of nums[idx]
        # what if the sign of nums[idx] is neg in the original array?
        # replace neg num by 0 as they are useless anyway
        # O(n), O(n)
        # for i, num in enumerate(nums):
        #     if num < 0:
        #         nums[i] = 0

        # for num in nums:
        #     num = abs(num)
        #     if 0 < num <= len(nums):
        #         if nums[num - 1] == 0:
        #             nums[num - 1] = -1
        #         nums[num - 1] = -abs(nums[num - 1])
        
        # i = 1
        # print(nums)
        # while i <= len(nums) and nums[i - 1] < 0:
        #     i += 1
        # return i

        # Solution 3: Cycle Sort
        i = 0
        while i < len(nums):
            if not 0 <= nums[i] - 1 < len(nums):
                i += 1
                continue
            if nums[i] == i + 1:
                i += 1
                continue
            num = nums[i]
            if num == nums[num - 1]:
                i += 1
                continue
            nums[num - 1], nums[i] = nums[i], nums[num - 1]


        
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                break
            i += 1
        return i + 1
            
            

