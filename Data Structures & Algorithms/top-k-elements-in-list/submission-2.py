class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        count_to_num = self.get_count_to_num(counter)
        top_k = []
        for i in range(max(count_to_num), 0, -1):
            top_k.extend(count_to_num[i])
        return top_k[:k]

    
    def get_count_to_num(self, counter):
        count_to_num = collections.defaultdict(list)
        for num in counter:
            count = counter[num]
            count_to_num[count].append(num)
        return count_to_num