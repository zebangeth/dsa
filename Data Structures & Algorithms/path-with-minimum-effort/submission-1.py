class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        heap = [(0, 0, 0)]
        max_diff = 0
        while heap:
            diff, r, c = heapq.heappop(heap)
            visited.add((r, c))
            max_diff = max(max_diff, diff)
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return max_diff

            for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not 0 <= nr < len(heights) or not 0 <= nc < len(heights[0]):
                    continue
                if (nr, nc) in visited:
                    continue
                ndiff = abs(heights[nr][nc] - heights[r][c])
                heapq.heappush(heap, (ndiff, nr, nc))

        

