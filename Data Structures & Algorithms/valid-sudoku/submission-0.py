class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.row_valid(board) and self.col_valid(board) and self.grid_valid(board)
    
    def row_valid(self, board):
        return all(self.check_valid(row) for row in board)
    
    def col_valid(self, board):
        for c in range(9):
            col = [board[r][c] for r in range(9)]
            if not self.check_valid(col):
                return False
        return True
    
    def grid_valid(self, board):
        # Validate each 3x3 sub-grid.
        # Top-left corners of each sub-grid are:
        # (0,0), (0,3), (0,6), (3,0), ..., (6,6)
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                grid = [
                    board[i][j]
                    for i in range(r, r + 3)
                    for j in range(c, c + 3)
                ]
                if not self.check_valid(grid):
                    return False
        return True

    def check_valid(self, strs):
        unique = set()
        for s in strs:
            if s != "." and s in unique:
                return False
            unique.add(s)
        return True
