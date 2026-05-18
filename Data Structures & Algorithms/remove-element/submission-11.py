class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i, j = 0, len(nums) - 1

        while i <= j:
            while i <= j and nums[i] != val:
                i += 1

            while i <= j and nums[j] == val:
                j -= 1

            if i > j:
                break

            nums[i], nums[j] = nums[j], nums[i]

            # Move both pointers inward to continue searching.
            # i += 1
            # j -= 1

        return i
