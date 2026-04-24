class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return -1
        maj = -1
        count = 0
        for num in nums:
            if maj == -1:
                maj, count = num, 1
            if maj == num:
                count += 1
            else:
                if count == 1: maj, count = -1, 0
                else: count -= 1
        return maj


        
