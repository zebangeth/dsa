class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        res = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in prefix_sum:
                res += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        return res
