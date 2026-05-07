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
            found_diff = False
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegrees[w2[j]] += 1
                    found_diff = True
                    break

            if not found_diff and len(w1) > len(w2):
                return None, None

        return indegrees, graph