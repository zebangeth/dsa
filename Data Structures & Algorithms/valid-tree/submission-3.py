class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = self.build_graph(n, edges)
        visited = set()
        if not self.dfs(0, -1, graph, visited):
            return False
        return len(visited) == n
    
    def dfs(self, cur, parent, graph, visited):
        visited.add(cur)
        for nxt in graph[cur]:
            if nxt == parent:
                continue
            if nxt in visited:
                return False
            if not self.dfs(nxt, cur, graph, visited):
                return False
        return True


    def build_graph(self, n, edges):
        graph = {node:set() for node in range(n)}
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        return graph