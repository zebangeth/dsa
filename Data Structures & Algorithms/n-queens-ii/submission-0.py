class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        self.dfs(0, set(), set(), set(), n)
        return self.ans
    
    def dfs(self, row, cols, diags, adiags, n):
        if row == n:
            self.ans += 1
            return
        
        for col in range(n):
            diag = row - col
            adiag = row + col
            if col in cols or diag in diags or adiag in adiags:
                continue

            cols.add(col)
            diags.add(diag)
            adiags.add(adiag)
            self.dfs(row + 1, cols, diags, adiags, n)
            cols.remove(col)
            diags.remove(diag)
            adiags.remove(adiag)
