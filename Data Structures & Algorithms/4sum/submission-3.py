class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        return self.k_sum(sorted_nums, target, 4, 0)

        
    def k_sum(self, nums, target, k, start):
        if k == 2:
            return self.two_sum(nums, target, start)
        
        if start >= len(nums) - 1:
            return []
        result = []

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            partials = self.k_sum(nums, target - nums[i], k - 1, i + 1)
            for partial in partials:
                result.append([nums[i]] + partial)
        
        return result
        
    def two_sum(self, nums, target, start):
        partials = []
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                partials.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return partials

