class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegrees, graph = self.build_graph(words)
        if not indegrees:
            return ""

        starts = []
        for w in indegrees:
            if indegrees[w] == 0:
                starts.append(w)
        
        queue = collections.deque(starts)
        sequence = starts[:]
        while queue:
            for _ in range(len(queue)):
                c = queue.popleft()
                for cn in graph[c]:
                    indegrees[cn] -= 1
                    if indegrees[cn] == 0:
                        queue.append(cn)
                        sequence.append(cn)
        
        return "".join(sequence) if len(sequence) == len(indegrees) else ""


    def build_graph(self, words):
        chars = "".join(words)
        indegrees = {c: 0 for c in chars}
        graph = collections.defaultdict(set)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for i, c in enumerate(w1):
                if len(w2) <= i:
                    return None, None
                if w2[i] == c:
                    continue
                if w2[i] not in graph[c]:
                    graph[c].add(w2[i])
                    indegrees[w2[i]] += 1
                break
        return indegrees, graph

