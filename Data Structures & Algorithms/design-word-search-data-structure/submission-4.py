class TrieNode:

    def __init__(self):
        self.children = dict()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)
    
    def _dfs(self, word, i, node):
        if i == len(word):
            return node.is_word
        
        if word[i] == '.':
            for child in node.children:
                if self._dfs(word, i + 1, node.children[child]):
                    return True
        else:
            if word[i] not in node.children:
                return False
            return self._dfs(word, i + 1, node.children[word[i]])
        return False
        
        
        
