class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        
        result = []
        for i, num in enumerate(sorted_nums):
            if num > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            two_sums = self.two_sum(sorted_nums, -num, i + 1)
            for two_sum_result in two_sums:
                result.append([num, two_sum_result[0], two_sum_result[1]])
        return result


    def two_sum(self, nums, target, start):
        results = []
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                results.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums [r + 1]:
                    r -= 1
        return results
        
        