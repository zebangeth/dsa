sys.setrecursionlimit(10**6)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = dict()
        lip = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                lip = max(lip, self.dfs(matrix, r, c, memo))
        return lip
        
    def dfs(self, grid, r, c, memo):
        if (r, c) in memo:
            return memo[(r, c)]
        
        path_len = 1
        for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                continue
            if grid[nr][nc] > grid[r][c]:
                path_len = max(
                    path_len, 
                    1 + self.dfs(grid, nr, nc, memo)
                )
        
        memo[(r, c)] = path_len
        return path_len