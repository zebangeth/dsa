class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        max_water = 0
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        while heap:
            water, r, c = heapq.heappop(heap)
            visited.add((r, c))
            max_water = max(max_water, water)
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return max_water
            for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue
                if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                    continue
                heapq.heappush(heap, (grid[nr][nc], nr, nc))
        