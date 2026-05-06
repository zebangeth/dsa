class Solution:
    def networkDelayTime(self, times, n, k):
        graph = self.build_graph(times, n)

        heap = [(0, k)]
        visited = set()

        total_time = 0

        while heap:
            time, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            total_time = max(total_time, time)
            for v in graph[u]:
                if v not in visited:
                    heapq.heappush(
                        heap,
                        (time + graph[u][v], v)
                    )

        return total_time if len(visited) == n else -1

    def build_graph(self, times, n):
        graph = {i: dict() for i in range(1, n + 1)}

        for u, v, t in times:
            graph[u][v] = t

        return graph