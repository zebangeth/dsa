class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        results = []
        for (a, b) in queries:
            results.append(self.dfs(a, b, 1, graph, set()))
        return results

    def build_graph(self, equations, values):
        graph = collections.defaultdict(dict)
        for i in range(len(values)):
            a, b = equations[i]
            val = values[i]
            graph[a][b] = val
            graph[b][a] = 1 / val
        return graph
    
    def dfs(self, a, b, div_val, graph, visited):
        if a not in graph or b not in graph:
            return -1

        if a == b:
            return 1 * div_val

        for nxt in graph[a]:
            if nxt in visited:
                continue
            visited.add(nxt)
            result = self.dfs(nxt, b, div_val * graph[a][nxt], graph, visited)
            if result != -1:
                return result
            visited.remove(nxt)
        return -1


