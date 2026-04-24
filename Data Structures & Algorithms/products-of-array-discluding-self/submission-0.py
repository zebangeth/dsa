class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1] * (len(nums) + 1), [1] * (len(nums) + 1)
        #build prefix & suffix product
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] * nums[i]
        for j in range(len(nums)-1, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j]
        print(prefix, suffix)
        return [prefix[i] * suffix[i+1] for i in range(len(nums))]

        