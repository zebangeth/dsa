class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        heap = [(0, 0, 0)]  # effort, row, col
        visited = set()

        while heap:
            effort, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == rows - 1 and c == cols - 1:
                return effort

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if (nr, nc) in visited:
                    continue

                edge_diff = abs(heights[nr][nc] - heights[r][c])
                new_effort = max(effort, edge_diff)

                heapq.heappush(heap, (new_effort, nr, nc))