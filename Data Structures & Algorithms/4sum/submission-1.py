class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        return self.k_sum(4, sorted_nums, target, 0)

    def k_sum(self, k, nums, target, start):
        """
        return the valid list of nums that sum up to target
        """
        if len(nums) - start < k:
            return []
        if nums[start] > (target / k) or nums[-1] < (target / k): 
            return []
        if k == 2:
            return self.two_sum(nums, target, start)
        result = []
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            for valid in self.k_sum(k - 1, nums, target - nums[i], i + 1):
                result.append([nums[i]] + valid)
        return result


    def two_sum(self, nums, target, start): 
        l, r = start, len(nums) - 1
        result = []
        while l < r:
            s = nums[l] + nums[r]
            if s < target or (l > start and nums[l] == nums[l - 1]):
                l += 1
            elif s > target or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                result.append([nums[l], nums[r]])
                l += 1
                r -= 1
        return result