class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            complement_num = target - num
            if complement_num in seen:
                return [seen[complement_num], i]
            seen[num] = i
        return []