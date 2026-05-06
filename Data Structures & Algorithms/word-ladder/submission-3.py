class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = self.build_graph(wordList + [beginWord])
        if endWord not in graph:
            return 0

        queue = collections.deque([beginWord])
        visited = set([beginWord])
        step = 1
        while queue:
            step += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                for nxt in graph[cur]:
                    if nxt in visited:
                        continue
                    if nxt == endWord:
                        return step
                    visited.add(nxt)
                    queue.append(nxt)
        return 0

    def build_graph(self, wordList):
        graph = collections.defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if not self.is_adj(wordList[i], wordList[j]):
                    continue
                graph[wordList[i]].add(wordList[j])
                graph[wordList[j]].add(wordList[i])
        return graph
    
    def is_adj(self, w1, w2):
        diff = 0
        for i, c in enumerate(w1):
            if w2[i] != c:
                diff += 1
            if diff > 1: return False
        return diff == 1