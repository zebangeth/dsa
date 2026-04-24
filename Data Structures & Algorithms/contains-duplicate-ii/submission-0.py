class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        unique = set()
        for i in range(len(nums)):
            if nums[i] in unique:
                return True
            unique.add(nums[i])

            if i >= k:
                unique.remove(nums[i - k])
        return False
