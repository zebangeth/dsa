class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, cols - 1
        top, bottom = 0, rows - 1

        while left <= right and top <= bottom:
            # 1. 从左到右走 top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. 从上到下走 right col
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. 从右到左走 bottom row
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. 从下到上走 left col
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res