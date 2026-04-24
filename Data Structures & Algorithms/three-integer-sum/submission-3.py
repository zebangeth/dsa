class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                print(i)
                continue
            target = -nums[i]
            for res in self.two_sum(nums, target, i + 1):
                result.append([nums[i], res[0], res[1]])
        return result


    def two_sum(self, nums, target, start):
        l, r = start, len(nums) - 1
        result = []
        while l < r:
            if target == nums[l] + nums[r]:
                result.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif target < nums[l] + nums[r]:
                r -= 1
            else:
                l += 1

        return result