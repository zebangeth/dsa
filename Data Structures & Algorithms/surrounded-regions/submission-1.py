class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != 'O':
                    continue
                region = set()
                if self.is_surrounded(board, r, c, region):
                    self.paint_surrounded(board, region)
        return

    
    def is_surrounded(self, board, r, c, region):
        queue = collections.deque([(r, c)])
        region.add((r, c))
        while queue:
            (r, c) = queue.popleft()
            for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if (new_r, new_c) in region:
                    continue
                if not 0 <= new_r < len(board) or not 0 <= new_c < len(board[0]):
                    return False
                if board[new_r][new_c] == 'O':
                    region.add((new_r, new_c))
                    queue.append((new_r, new_c))
        return True
    
    def paint_surrounded(self, board, region):
        for (r, c) in region:
            board[r][c] = 'X'
        return
                
