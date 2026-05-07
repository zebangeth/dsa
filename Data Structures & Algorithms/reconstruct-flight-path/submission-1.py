class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        counter = collections.Counter([(src, dst) for (src, dst) in tickets])

        # lexical order
        for src, dst in sorted(tickets):
            graph[src].append(dst)

        self.res = []
        self.total = len(tickets)

        self.backtrack("JFK", graph, counter, ["JFK"])

        return self.res

    def backtrack(self, src, graph, counter, path):

        # 已经找到答案
        if self.res:
            return

        # 用完所有 tickets
        if len(path) == self.total + 1:
            self.res = path[:]
            return

        for dst in graph[src]:
            # 这张票已经用完
            if counter[(src, dst)] == 0:
                continue

            counter[(src, dst)] -= 1
            path.append(dst)
            self.backtrack(dst, graph, counter, path)
            path.pop()
            counter[(src, dst)] += 1
