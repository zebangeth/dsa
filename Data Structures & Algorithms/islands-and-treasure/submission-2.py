class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        treasures = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    treasures.append((r, c))
        
        queue = collections.deque(treasures)
        dist = 0
        while queue:
            dist += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                        continue
                    if grid[nr][nc] != INF:
                        continue
                    grid[nr][nc] = dist
                    queue.append((nr, nc))
