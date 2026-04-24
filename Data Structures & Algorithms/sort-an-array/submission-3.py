class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        self._quick_sort(nums, 0, len(nums) - 1)
        return nums
    
    def _quick_sort(self, nums, start, end):
        if start >= end:
            return

        l, r = start, end
        pivot = nums[(l + r) // 2]
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        self._quick_sort(nums, start, r)
        self._quick_sort(nums, l, end)



# class Solution: 
#     def sort_integers(self, arr): 
#         if arr is None or len(arr) == 0: 
#             return 
#         self.quick_sort_helper(arr, 0, len(arr) - 1)
    
#     def quick_sort_helper(self, l_arr, start, end): 
#         if start >= end: 
#             return
        
#         left, right = start, end
#         # 1. pivot 尽量居中，或者直接生成随机索引 pivot = arr[random.randint(start, end)]
#         pivot = l_arr[(start + end) // 2]
        
#         # 2. left <= right 而不能是 left < right, 否则递归可能永远无法停止
#         while left <= right: 
#             # 3. l_arr[left] < pivot 不能用 <= 否则会
#             # 规律是 left 和 right 比用 <=, 和 pivot 比用 > / < 不用 >= / <=
#             while left <= right and l_arr[left] < pivot: 
#                 left += 1
#             while left <= right and l_arr[right] > pivot: 
#                 right -= 1
#             if left <= right: 
#                 l_arr[left], l_arr[right] = l_arr[right], l_arr[left]
#                 left += 1
#                 right -= 1
                    
#         self.quick_sort_helper(l_arr, start, right)
#         self.quick_sort_helper(l_arr, left, end)