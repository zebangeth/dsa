class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        self.dfs(n, [], 0, set(), set(), set())
        return self.results


    def dfs(self, n, board, r, cols, diags, adiags):
        if r == n:
            self.results.append(board[:])
            return
        
        for c in range(n):
            if c in cols or r - c in diags or r + c in adiags:
                continue
            row = ['.'] * n
            row[c] = 'Q'
            board.append("".join(row))
            cols.add(c)
            diags.add(r - c)
            adiags.add(r + c)
            self.dfs(n, board, r + 1, cols, diags, adiags)
            board.pop()
            cols.remove(c)
            diags.remove(r - c)
            adiags.remove(r + c)
            

