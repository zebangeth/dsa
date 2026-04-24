class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # result = []
        # counter = collections.Counter(nums)
        # for num in counter:
        #     if counter[num] > len(nums) / 3:
        #         result.append(num)
        # return result

        if len(nums) <= 2:
            return list(set(nums))
        
        freq = {}
        for num in nums:
            freq = self.update_freq(freq, num)
        
        result = []
        for num in freq:
            if self.count(num, nums) > len(nums) / 3:
                result.append(num)
        return result
    
    def update_freq(self, freq, num):
        if num in freq:
            freq[num] += 1
            return freq
        
        if len(freq) < 2:
            freq[num] = 1
            return freq
        
        p, q = list(freq.keys())
        freq[p] -= 1
        freq[q] -= 1
        
        if freq[p] == 0:
            freq.pop(p)
        if freq[q] == 0:
            freq.pop(q)
        
        return freq
    
    def count(self, num, nums):
        count = 0
        for n in nums:
            if n == num:
                count += 1
        return count


