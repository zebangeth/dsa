class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = [] # (idx, h)
        max_area = 0
        for idx, h in enumerate(heights):
            pre_i = idx
            while mono_stack and mono_stack[-1][1] >= h:
                pre_i, pre_h = mono_stack.pop()
                area = (idx - pre_i) * pre_h
                max_area = max(area, max_area)
                print(pre_i, pre_h, idx, h, area)
            mono_stack.append((pre_i, h))
        
        while mono_stack:
            pre_i, pre_h = mono_stack.pop()
            area = (len(heights) - pre_i) * pre_h
            max_area = max(area, max_area)
            print(pre_i, pre_h, h, area)

        
        return max_area
