class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        max_area = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 1 or (r, c) in visited:
                    continue
                area = self.explore(grid, r, c, visited)
                print(r, c, area)
                max_area = max(max_area, area)
        
        return max_area
    
    def explore(self, grid, r, c, visited):        
        queue = collections.deque([(r, c)])
        visited.add((r, c))
        area = 0
        while queue:
            cur_r, cur_c = queue.popleft()
            area += 1
            for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = cur_r + dr, cur_c + dc
                if not 0 <= new_r < len(grid) or not 0 <= new_c < len(grid[0]):
                    continue
                if (new_r, new_c) in visited or grid[new_r][new_c] != 1:
                    continue
                queue.append((new_r, new_c))
                visited.add((new_r, new_c))
        
        return area
