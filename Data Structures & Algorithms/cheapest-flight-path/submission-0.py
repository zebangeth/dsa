class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]

            for u, v, price in flights:
                if prices[u] == INF:
                    continue
                temp[v] = min(temp[v], prices[u] + price)

            prices = temp

        return -1 if prices[dst] == INF else prices[dst]