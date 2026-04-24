import collections

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words: 
            return ""

        self.invalid = False
        graph = self.build_graph(words)
        indegrees = self.find_indegrees(graph, words)
        queue = collections.deque([c for c in indegrees if indegrees[c] == 0])
        res_dict = []
        
        while queue:
            cur = queue.popleft()
            res_dict.append(cur)
            for nxt in graph[cur]: 
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0: 
                    queue.append(nxt)
        
        # check indegrees
        for c in indegrees: 
            if indegrees[c] != 0: 
                self.invalid = True
        return "".join(res_dict) if not self.invalid else "" 
    
    def build_graph(self, words): 
        graph = collections.defaultdict(list)
        for i in range(len(words) - 1): 
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))): 
                if j == min(len(w1), len(w2)) - 1 and w1[j] == w2[j]: 
                    if len(w1) > len(w2): 
                        self.invalid = True
                        break
                if w1[j] == w2[j]: 
                    continue
                graph[w1[j]].append(w2[j])
                break

        return graph
    
    def find_indegrees(self, graph, words): 
        all_c = set("".join(words))
        indegrees = {c: 0 for c in all_c}
        for c in graph: 
            for x in graph[c]: 
                indegrees[x] += 1
        return indegrees