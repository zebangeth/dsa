class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = self.build_graph(points)

        frontier = [(0, 0)]
        visited = set()
        total_cost = 0
        while frontier:
            cost, p = heapq.heappop(frontier)
            if p in visited:
                continue
            visited.add(p)
            total_cost += cost
            for (cost, nei) in graph[p]:
                if nei in visited:
                    continue
                heapq.heappush(frontier, (cost, nei))
        return total_cost

    def build_graph(self, points):
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        return graph
            
