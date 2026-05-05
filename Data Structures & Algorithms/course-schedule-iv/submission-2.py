class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:
        graph = self.build_graph(numCourses, prerequisites)
        memo = {}

        result = []
        for pre, nxt in queries:
            reachable = self.get_reachable(pre, graph, memo)
            result.append(nxt in reachable)

        return result

    def build_graph(self, numCourses, prerequisites):
        graph = {course: set() for course in range(numCourses)}

        for pre, nxt in prerequisites:
            graph[pre].add(nxt)

        return graph

    def get_reachable(self, course, graph, memo):
        if course in memo:
            return memo[course]

        reachable = set()

        for nxt in graph[course]:
            reachable.add(nxt)
            reachable |= self.get_reachable(nxt, graph, memo)

        memo[course] = reachable
        return reachable