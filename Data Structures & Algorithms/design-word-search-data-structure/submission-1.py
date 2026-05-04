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
        return self.__dfs(word, self.root, 0)

        
    def __dfs(self, word, node, start):
        if not word or len(word) == start:
            return node.is_word
        
        for i in range(start, len(word)):
            c = word[i]
            if c == '.':
                for child in node.children:
                    if self.__dfs(word, node.children[child], i + 1):
                        return True
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.is_word