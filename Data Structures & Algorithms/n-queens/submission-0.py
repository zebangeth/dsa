class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.solutions = []
        board = [['.'] * n for _ in range(n)]
        self.dfs(0, set(), set(), set(), board, n)
        return self.solutions
    
    def dfs(self, row, cols, diags, anti_diags, board, n):
        if row == n:
            board = [''.join(r) for r in board]
            self.solutions.append(board)
            return

        for col in range(n):
            diag = row - col
            anti_diag = row + col
            if col in cols or diag in diags or anti_diag in anti_diags:
                continue
            cols.add(col)
            diags.add(diag)
            anti_diags.add(anti_diag)
            board[row][col] = 'Q'
            self.dfs(row + 1, cols, diags, anti_diags, board, n)
            board[row][col] = '.'
            cols.remove(col)
            diags.remove(diag)
            anti_diags.remove(anti_diag)
