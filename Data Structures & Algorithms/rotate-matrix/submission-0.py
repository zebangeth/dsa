class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        # flip over diag
        for r in range(rows):
            for c in range(r, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # flip over middle
        for r in range(rows):
            for c in range(cols // 2):
                matrix[r][c], matrix[r][cols - 1 - c] = matrix[r][cols - 1 - c], matrix[r][c]

