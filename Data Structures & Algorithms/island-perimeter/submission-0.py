class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_border = 0
        shared_border = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    total_border += 4
                    shared_border += self.check_adj(grid, r, c)
        
        return total_border - shared_border
                

    def check_adj(self, grid, r, c):
        adj = 0
        for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r, new_c = r + dr, c + dc
            if not 0 <= new_r < len(grid) or not 0 <= new_c < len(grid[0]):
                continue
            if grid[new_r][new_c] == 1:
                adj += 1

        return adj
