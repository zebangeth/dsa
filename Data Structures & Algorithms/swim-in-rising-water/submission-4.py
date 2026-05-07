class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        start = 0
        end = max(grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])))

        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_possible(grid, 0, 0, mid, {(0, 0)}):
                end = mid
            else:
                start = mid

        if self.is_possible(grid, 0, 0, start, {(0, 0)}):
            return start
        return end

    def is_possible(self, grid, r, c, t, visited):
        if grid[r][c] > t:
            return False
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                continue
            if (nr, nc) in visited:
                continue
            if grid[nr][nc] > t:
                continue
            visited.add((nr, nc))
            if self.is_possible(grid, nr, nc, t, visited):
                return True
        return False