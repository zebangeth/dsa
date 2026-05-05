class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set([(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)])
        atl = set([(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)])

        pac_acc = self.bfs(heights, pac)
        atl_acc = self.bfs(heights, atl)
        return list(pac_acc & atl_acc)


    def bfs(self, grid, starts):
        """
        return the accessible points in grid
        """
        queue = collections.deque(starts)
        visited = set(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if (
                    (new_r, new_c) in visited
                    or not 0 <= new_r < len(grid)
                    or not 0 <= new_c < len(grid[0])
                    or grid[new_r][new_c] < grid[r][c]
                ):
                    continue
                queue.append((new_r, new_c))
                visited.add((new_r, new_c))
        return visited

            
            

