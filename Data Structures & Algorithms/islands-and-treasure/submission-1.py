class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647

        treasures = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    treasures.append((r, c))
        
        queue = collections.deque(treasures)
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r + dr, c + dc
                    if not 0 <= new_r < len(grid) or not 0 <= new_c < len(grid[0]):
                        continue
                    if grid[new_r][new_c] != land:
                        continue
                    grid[new_r][new_c] = distance
                    queue.append((new_r, new_c))

        return