# 1st step: Implement trie
class TrieNode: 
    def __init__(self): 
        self.children = dict()
        self.is_word = False
        self.word = None

class WordDict: 
    def __init__(self): 
        self.root = TrieNode()
    
    def add_word(self, word): 
        cur = self.root
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 2nd step: Store all words into a trie
        word_dict = WordDict()
        for word in words: 
            word_dict.add_word(word)
        
        self.output = set() # set() - there might be multiple paths to get the same word
        root = word_dict.root
        # 3rd step: Search each cell using a dfs approach
        for r in range(len(board)): 
            for c in range(len(board[0])):
                self._dfs(r, c, root, board, set())    
        
        return list(self.output)
    
    def _dfs(self, r, c, node, board, visited):
        if not self._is_valid(r, c, node, board, visited): 
            return
        
        char = board[r][c]
        node = node.children[char]
        if node.is_word:
            self.output.add(node.word)
        visited.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            self._dfs(r + dr, c + dc, node, board, visited)
        visited.remove((r, c))
    
    def _is_valid(self, r, c, node, board, visited):
        return (
            0 <= r < len(board)
            and 0 <= c < len(board[0])
            and (r, c) not in visited
            and board[r][c] in node.children
        )
