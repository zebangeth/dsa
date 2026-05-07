class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        if n < 3:
            return nums[n]

        for i in range(n - 2):
            t_nxt = sum(nums)
            nums[0], nums[1], nums[2] = nums[1], nums[2], t_nxt

        return nums[-1]
