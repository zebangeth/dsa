class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # efforts to reach (r, c)
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        heap = [(0, 0, 0)] # effort, r, c
        while heap:
            effort, r, c = heapq.heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return effort
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < rows or not 0 <= nc < cols:
                    continue
                neffort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                if neffort < efforts[nr][nc]:
                    heapq.heappush(heap, (neffort, nr, nc))
                    efforts[nr][nc] = neffort


