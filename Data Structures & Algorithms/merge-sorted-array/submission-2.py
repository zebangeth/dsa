class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p1, p2 = 0, 0
        # res = []
        # while p1 < m and p2 < len(nums2):
        #     if nums1[p1] < nums2[p2]:
        #         res.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         res.append(nums2[p2])
        #         p2 += 1
            
            
        # if p1 < m:
        #     res.extend(nums1[p1:])
        # if p2 < len(nums2):
        #     res.extend(nums2[p2:])
        # for i in range(len(nums1)):
        #     nums1[i] = res[i]
        
        # Solution 2: merge in reverse order, 
        # 3 pointers, without extra memory
        p1, p2, nxt = m - 1, len(nums2) - 1, len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[nxt] = nums1[p1]
                p1 -= 1
            else:
                nums1[nxt] = nums2[p2]
                p2 -= 1
            nxt -= 1
        
        while p2 >= 0:
            nums1[nxt] = nums2[p2]
            p2 -= 1
            nxt -= 1


            