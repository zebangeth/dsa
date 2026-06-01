class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_map = self.build_word_map(wordList + [beginWord])
        
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        path_len = 0
        while queue:
            path_len += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return path_len
                for nei in word_map[cur]:
                    if nei in visited:
                        continue
                    queue.append(nei)
                    visited.add(nei)
        return 0

    def build_word_map(self, words):
        word_map = collections.defaultdict(set)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.is_connected(words[i], words[j]):
                    word_map[words[i]].add(words[j])
                    word_map[words[j]].add(words[i])
        return word_map
    
    def is_connected(self, word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
            if diff > 1:
                return False
        return True