class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1


        queue = collections.deque(rotten)
        minutes = 0
        visited = set()
        while queue:
            infected_this_round = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_r, new_c = r + dr, c + dc
                    if not 0 <= new_r < len(grid) or not 0 <= new_c < len(grid[0]):
                        continue
                    if grid[new_r][new_c] != 1 or (new_r, new_c) in visited:
                        continue
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
                    infected_this_round = True

            if infected_this_round:
                minutes += 1

        return minutes if len(visited) == fresh else -1