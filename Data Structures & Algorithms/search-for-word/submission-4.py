DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False
        
        board_chars = []
        for row in board:
            board_chars.extend(row)
        counter_board = collections.Counter(board_chars)
        counter_word = collections.Counter(word)
        for key in counter_word:
            if counter_word[key] > counter_board[key]:
                return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.find(board, r, c, word, set([(r, c)])):
                    return True
        return False
    

    def find(self, board, r, c, word, visited):
        if len(word) == 0 or len(word) == 1 and word[0] == board[r][c]:
            return True

        if word[0] != board[r][c]:
            return False
        
        for (dr, dc) in DIRECTIONS:
            new_r, new_c = r + dr, c + dc
            if not 0 <= new_r < len(board) or not 0 <= new_c < len(board[0]):
                continue
            if (new_r, new_c) in visited:
                continue
            if self.find(board, new_r, new_c, word[1:], visited | set([(new_r, new_c)])):
                return True
        return False
        

