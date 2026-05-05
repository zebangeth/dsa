class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = self.build_graph(n, edges)

        queue = collections.deque([(0, -1)])  # (current node, parent node)
        visited = set([0])
        while queue:
            cur, parent = queue.popleft()
            for adj in graph[cur]:
                if adj == parent:
                    continue
                if adj in visited:
                    return False
                visited.add(adj)
                queue.append((adj, cur))
        
        return len(visited) == n

    def build_graph(self, n, edges):
        graph = {node:set() for node in range(n)}
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        return graph