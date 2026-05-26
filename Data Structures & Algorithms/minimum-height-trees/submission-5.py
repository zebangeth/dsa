class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        graph = collections.defaultdict(set)
        connected_nodes = collections.defaultdict(int)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
            connected_nodes[n1] += 1
            connected_nodes[n2] += 1
        
        leaves = []
        for node in connected_nodes:
            if connected_nodes[node] == 1:
                leaves.append(node)
        print(leaves)
        
        queue = collections.deque(leaves)
        visited = set(leaves)
        last_nodes = -1
        while queue:
            last_nodes = list(queue)
            for _ in range(len(queue)):
                last_node = queue.popleft()
                for nxt in graph[last_node]:
                    if nxt in visited:
                        continue
                    connected_nodes[nxt] -= 1
                    if connected_nodes[nxt] == 1:
                        queue.append(nxt)
                        visited.add(nxt)
        return last_nodes


