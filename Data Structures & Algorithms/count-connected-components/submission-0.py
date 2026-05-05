class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.build_graph(n, edges)

        visited = set()
        count = 0
        for node in graph:
            if node in visited:
                continue
            visited.add(node)
            self.dfs(graph, node, visited)
            count += 1
        return count

    def dfs(self, graph, node, visited):
        for nxt in graph[node]:
            if nxt in visited:
                continue
            visited.add(nxt)
            self.dfs(graph, nxt, visited)
            
        
    def build_graph(self, n, edges):
        graph = {i: set() for i in range(n)}
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        return graph