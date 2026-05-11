class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        steps = 0
        i, max_pos = 0, nums[0]
        while i < len(nums):
            max_next_pos = 0
            while i < len(nums) and i <= max_pos:
                max_next_pos = max(max_next_pos, i + nums[i])
                i += 1
            max_pos = max_next_pos
            steps += 1
        return steps
