class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[j] == val:
                j -= 1
                continue
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        while j > 0 and nums[j] == val:
            j -= 1
        return j + 1
            
