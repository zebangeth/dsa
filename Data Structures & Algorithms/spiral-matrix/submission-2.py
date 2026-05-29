class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        while top <= bottom and left <= right:
            # top left to right
            for c in range(left, right  + 1):
                print(top, c, matrix[top][c])
                result.append(matrix[top][c])
            top += 1
            
            # right top to bottom
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # bottom right to left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            
            # left bottom to top
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
