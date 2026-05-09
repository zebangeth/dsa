sys.setrecursionlimit(10**6)

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        global_lip = 0
        memo = dict() # (r, c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                global_lip = max(global_lip, self.dfs(r, c, matrix, memo))
        return global_lip
    
    def dfs(self, r, c, matrix, memo):
        if (r, c) in memo:
            return memo[(r, c)]
        
        lip = 1
        for (dr, dc) in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if not 0 <= nr < len(matrix) or not 0 <= nc < len(matrix[0]):
                continue
            if matrix[nr][nc] > matrix[r][c]:
                lip = max(lip, self.dfs(nr, nc, matrix, memo) + 1)
        memo[(r, c)] = lip
        return lip


    def is_end(self, r, c, matrix):
        for (dr, dc) in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if not 0 <= nr < len(matrix) or not 0 <= nc < len(matrix[0]):
                continue
            if matrix[nr][nc] > matrix[r][c]:
                return False
        return True