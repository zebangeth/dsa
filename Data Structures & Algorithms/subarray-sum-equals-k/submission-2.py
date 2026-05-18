class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_count[p] = number of times prefix sum p has appeared so far
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # empty prefix

        prefix_sum = 0
        answer = 0

        for num in nums:
            prefix_sum += num
            answer += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1

        return answer