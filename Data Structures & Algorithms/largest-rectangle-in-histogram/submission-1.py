class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # (start_idx, height)
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            # 如果当前柱子高度小于栈顶柱子高度
            if stack and stack[-1][1] > h:
                # 维护 monotonic stack
                while stack and stack[-1][1] > h:
                    prev_i, prev_h = stack.pop()
                    # 以 prev_h 为高所对应的矩形结束了，计算面积
                    max_area = max((i - prev_i) * prev_h, max_area)
                # 因为 pop 的柱子都比当前柱子高，所以以当前柱子为高度对应的矩形
                # 可以从 prev_i 开始计算
                i = prev_i
            stack.append((i, h))

        while stack:
            i, h = stack.pop()
            area = (len(heights) - i) * h
            max_area = max(max_area, area)
        return max_area
