class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.find_kth(nums1, nums2, total // 2 + 1)
        else:
            return (self.find_kth(nums1, nums2, total // 2) + self.find_kth(nums1, nums2, total // 2 + 1)) / 2

    def find_kth(self, nums1, nums2, k):
        # BASE
        # If one array is empty, return the k-th element from the other array
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        # If k is 1, return the smaller of the first elements of both arrays
        if k == 1:
            return min(nums1[0], nums2[0])

        # RECURSIVE
        # Discard the first k//2 elements of the array with the smaller compared element
        i = min(len(nums1), k // 2)
        j = min(len(nums2), k // 2)

        if nums1[i - 1] < nums2[j - 1]:
            return self.find_kth(nums1[i:], nums2, k - i)
        else:
            return self.find_kth(nums1, nums2[j:], k - j)