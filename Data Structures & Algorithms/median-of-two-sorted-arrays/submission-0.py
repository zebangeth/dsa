# 1. 通过二分查找，将较短的数组进行切分，确保左右两侧元素满足中位数的条件，即左侧的最大值小于右侧的最小值。
# 2. 根据总长度是奇数还是偶数，返回切分后的元素中符合条件的单一元素或两个元素的平均值作为中位数。

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        odd = (total % 2 == 1)
        half = total // 2

        # make nums1 the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        while True:
            i1 = (l + r) // 2
            i2 = half - i1 - 2

            # 假设 nums1 和 nums2 的左侧都有一个 -inf 右侧都有一个 inf 方便 edge case:
            # e.g. nums1 = [10, 20, 30, 40], nums2 = [1, 2, 3, 4, 5, 6]
            left_max1 = nums1[i1] if i1 >= 0 else -float('inf')
            right_min1 = nums1[i1 + 1] if i1 + 1 < len(nums1) else float('inf')
            left_max2 = nums2[i2] if i2 >= 0 else -float('inf')
            right_min2 = nums2[i2 + 1] if i2 + 1 < len(nums2) else float('inf')
            
            # 两个左侧部分的最大值都小于右侧部分的最小值，中位数就在中间
            if left_max1 <= right_min2 and left_max2 <= right_min1:
                if odd: 
                    return min(right_min1, right_min2)
                else: 
                    return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2
            # 如果 nums1 的左侧最大值大于 nums2 的右侧最小值，说明切分点 i1 过大，需向左调整
            elif left_max1 > right_min2: r = i1 - 1
            # 否则，向右调整切分点 i1
            else: l = i1 + 1