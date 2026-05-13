class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        r_zeros = [1] * rows
        c_zeros = [1] * cols
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    r_zeros[r] = 0
                    c_zeros[c] = 0
        
        for r in range(rows):
            for c in range(cols):
                if r_zeros[r] == 0 or c_zeros[c] == 0:
                    matrix[r][c] = 0
                    

