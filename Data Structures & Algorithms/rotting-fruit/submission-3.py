class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rottens.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        queue = collections.deque(rottens)
        mins = 0
        while queue:
            mins += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                        continue
                    if grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            

        return mins - 1 if fresh == 0 else -1

