class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        jumps = 0
        last_jump_step = nums[0]
        pos = 0
        while pos < len(nums) - 1:
            jumps += 1
            max_jump_i = -1
            max_jump_step = -1
            for i in range(pos, last_jump_step + 1):
                if i >= len(nums) - 1:
                    return jumps
                if nums[i] + i > max_jump_step:
                    max_jump_step = nums[i] + i
                    max_jump_i = i
            pos = max_jump_i
            last_jump_step = max_jump_step
        
        return jumps
