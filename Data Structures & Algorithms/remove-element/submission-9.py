class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Handle the edge case where the input list is empty.
        if not nums:
            return 0

        # Use two pointers:
        # i moves from the left to find an element equal to val
        # j moves from the right to find an element that is not val
        i, j = 0, len(nums) - 1

        # Continue until the pointers meet.
        # All elements to the right of j will be removed elements.
        while i <= j:
            # Move i rightward while it already points to a valid element.
            while i <= j and nums[i] != val:
                i += 1

            # Move j leftward while it already points to an element that should be removed.
            while i <= j and nums[j] == val:
                j -= 1

            # If the pointers have crossed, no more swaps are needed.
            if i > j:
                break

            # Swap the invalid element at i with the valid element at j.
            nums[i], nums[j] = nums[j], nums[i]

            # Move both pointers inward to continue searching.
            # i += 1
            # j -= 1

        # The new valid length is the number of elements before index i.
        # Since j ends at the last valid position, return j + 1.
        return j + 1


# Summary of issues and fixes:
# - The original loop condition used `while i < j`, which can miss the case where
#   the pointers meet on the last remaining element. It is safer to use `i <= j`.
# - The original code returned `j`, but the problem expects the count of remaining
#   valid elements, which is `j + 1`.
# - The original code did not advance the pointers after swapping, which could
#   lead to an infinite loop or repeated swapping of the same elements.
# - Added comments to clarify the purpose of each step and the two-pointer strategy.