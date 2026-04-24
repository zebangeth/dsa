import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        frq_to_nums = collections.defaultdict(list)
        for num, frq in count.items(): 
            frq_to_nums[frq].append(num)

        top_k = []
        for frq in range(len(nums), 0, -1): 
            top_k.extend(frq_to_nums[frq])
            if len(top_k) >= k:
                return top_k[:k]