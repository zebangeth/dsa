# Dijkstra
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Build graph
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # Priority queue: (cost, current node, stops)
        heap = [(0, src, 0)]
        # 这个 visited dictionary 也可以不用，因为当 heap 中没有 stops <= k + 1 的节点时本身也会自动停止
        # 这里 visited 的目的是进行剪枝，如果同样 stops 数量有更便宜的节点了就没必要重复处理
        # Dictionary to keep track of the minimum cost to reach a node with a certain number of stops
        visited = dict()
        
        while heap:
            cost, cur, stops = heapq.heappop(heap)
            
            # If stops exceed limit, continue
            if stops > k + 1:
                continue
            
            # If destination is reached, return cost
            if cur == dst:
                return cost
            
            # If we have already reached this node with fewer stops and lower cost, skip
            if (cur in visited and visited[cur] <= stops):
                continue
            visited[cur] = stops
            
            for neighbor, price in graph[cur]:
                # Push the new cost, neighbor, and updated stops into the heap
                heapq.heappush(heap, (cost + price, neighbor, stops + 1))
        
        return -1
