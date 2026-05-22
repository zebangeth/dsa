class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: set() for i in range(n)}
        connected = {i: 0 for i in range(n)}
        for (p1, p2) in edges:
            graph[p1].add(p2)
            graph[p2].add(p1)
            connected[p1] += 1
            connected[p2] += 1
        
        visited = set([0])
        queue = collections.deque([(0, -1)])
        while queue:
            cur, parent = queue.popleft()
            for nei in graph[cur]:
                if nei in visited and nei != parent:
                    return False
                if nei == parent:
                    continue
                queue.append((nei, cur))
                visited.add(nei)
        return len(visited) == n