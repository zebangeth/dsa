class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        surrounded = []
        self.visited = set()

        for r in range(1, len(board) - 1):
            for c in range(1, len(board[0]) - 1):
                if board[r][c] == 'X' or (r, c) in self.visited:
                    continue
                is_surrounded, explored = self.explore(r, c, board)
                if is_surrounded:
                    surrounded.extend(explored)
        
        self.paint(board, surrounded)


    def explore(self, r, c, board):
        is_surrounded = True
        explored = [(r, c)]
        queue = collections.deque([(r, c)])
        while queue:
            r, c = queue.popleft()
            for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in self.visited or not 0 <= nr < len(board) or not 0 <= nc < len(board[0]):
                    continue
                if board[nr][nc] == 'O':
                    queue.append((nr, nc))
                    self.visited.add((nr, nc))
                    explored.append((nr, nc))
                    if nr == 0 or nr == len(board) - 1 or nc == 0 or nc == len(board[0]) - 1:
                        is_surrounded = False
        return is_surrounded, explored
    
    def paint(self, board, surrounded):
        for (r, c) in surrounded:
            board[r][c] = 'X'
                        


