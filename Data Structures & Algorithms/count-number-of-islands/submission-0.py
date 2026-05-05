class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '0':
                    continue
                if (r, c) in visited:
                    continue
                islands += 1
                self.explore(grid, r, c, visited)
        
        return islands
    
    def explore(self, grid, r, c, visited):
        if not self.is_valid(grid, r, c, visited):
            return
        
        visited.add((r, c))
        for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            self.explore(grid, new_r, new_c, visited)
        
    
    def is_valid(self, grid, r, c, visited):
        return (
            0 <= r < len(grid) and
            0 <= c < len(grid[0]) and
            (r, c) not in visited and
            grid[r][c] == '1'
        )
        

