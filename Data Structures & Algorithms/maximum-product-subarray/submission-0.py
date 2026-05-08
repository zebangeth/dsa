class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            prev_max = max_prod
            prev_min = min_prod

            max_prod = max(num, prev_max * num, prev_min * num)
            min_prod = min(num, prev_max * num, prev_min * num)

            ans = max(ans, max_prod)

        return ans