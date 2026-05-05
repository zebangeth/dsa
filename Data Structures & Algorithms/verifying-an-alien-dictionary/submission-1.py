class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if not words:
            return True

        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            if not self.compare(words[i], words[i + 1], order_index):
                return False
        
        return True
    
    def compare(self, word1, word2, order_index):
        for i in range(len(word1)):
            if i >= len(word2):
                return False
            if word1[i] == word2[i]:
                continue
            elif order_index[word1[i]] < order_index[word2[i]]:
                return True
            else:
                return False
        return True