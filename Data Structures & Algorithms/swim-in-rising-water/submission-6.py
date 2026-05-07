DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], (0, 0))]
        visited = set()

        while heap:
            (cur_h, (r, c)) = heapq.heappop(heap)

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return cur_h
            for (dr, dc) in DIRECTIONS:
                new_r, new_c = r + dr, c + dc
                if not 0 <= new_r < len(grid) or not 0 <= new_c < len(grid[0]):
                    continue
                if (new_r, new_c) in visited:
                    continue
                heapq.heappush(heap, (max(cur_h, grid[new_r][new_c]), (new_r, new_c)))
                visited.add((new_r, new_c))