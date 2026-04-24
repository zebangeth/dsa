class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: 
            return True
        
        graph = self.build_graph(n, edges)
        visited = set([0])
        no_cycle = self.dfs(graph, 0, visited, -1)
        print(no_cycle)
        print(visited)
        return no_cycle and len(visited) == n


    def build_graph(self, n, edges): 
        graph = {i: set() for i in range(n)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        return graph

    def dfs(self, graph, i, visited, prev): 
        for neighbor in graph[i]: 
            if neighbor == prev: 
                continue
            if neighbor in visited: 
                return False
            visited.add(neighbor)
            if not self.dfs(graph, neighbor, visited, i): 
                return False
        return True
            
