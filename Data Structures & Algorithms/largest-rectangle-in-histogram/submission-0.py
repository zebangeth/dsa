class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # (start_idx, height)
        stack = []
        max_area = 0
        for i in range(len(heights)):
            prev_i = i
            while stack and heights[i] < stack[-1][1]:
                prev_i, prev_h = stack.pop()
                area = (i - prev_i) * prev_h
                max_area = max(max_area, area)
            stack.append((prev_i, heights[i]))

        while stack:
            i, h = stack.pop()
            area = (len(heights) - i) * h
            max_area = max(max_area, area)
        return max_area
