class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic increasing stack
        stack = [] # (height, index)
        max_area = 0
        for i, h in enumerate(heights + [0]):
            prv_i = i
            while stack and stack[-1][0] > h:
                prv_h, prv_i = stack.pop()
                area = (i - prv_i) * prv_h
                max_area = max(max_area, area)

            stack.append((h, prv_i))
        
        return max_area
