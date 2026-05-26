class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))

        heap = [(0, 0, src)] # cum_price, steps, dst
        visited = set()
        total = 0
        while heap:
            cum_price, steps, cur = heapq.heappop(heap)
            if steps > k + 1:
                continue
            visited.add(cur)
            if cur == dst:
                return cum_price
            for (nxt, price) in graph[cur]:
                if nxt in visited:
                    continue
                heapq.heappush(heap, (cum_price + price, steps + 1, nxt))

        return -1
            