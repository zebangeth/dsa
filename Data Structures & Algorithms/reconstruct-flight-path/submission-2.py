class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        counter = collections.Counter([(src, dst) for (src, dst) in tickets])

        for (start, end) in sorted(tickets):
            graph[start].append(end)
        
        self.path = ["JFK"]
        self.dfs(graph, counter, "JFK", len(tickets) + 1)
        return self.path
    
    def dfs(self, graph, counter, cur, leng):
        if len(self.path) == leng:
            return True
        
        for nxt in graph[cur]:
            if counter[(cur, nxt)] == 0:
                continue
            self.path.append(nxt)
            counter[(cur, nxt)] -= 1
            if self.dfs(graph, counter, nxt, leng):
                return True
            self.path.pop()
            counter[(cur, nxt)] += 1
        return False