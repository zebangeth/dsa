class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        counter = collections.Counter(nums)
        for num in counter:
            if counter[num] > len(nums) / 3:
                result.append(num)
        return result