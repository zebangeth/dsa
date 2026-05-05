class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        graph = self.build_graph(numCourses, prerequisites)
        reachable = [[False] * numCourses for _ in range(numCourses)]

        for course in range(numCourses):
            visited = set()
            self.dfs(course, course, graph, visited, reachable)

        return [reachable[u][v] for u, v in queries]

    def dfs(self, start, cur, graph, visited, reachable):
        for nxt in graph[cur]:
            if nxt in visited:
                continue

            visited.add(nxt)
            reachable[start][nxt] = True
            self.dfs(start, nxt, graph, visited, reachable)

    def build_graph(self, numCourses, prerequisites):
        graph = {course: [] for course in range(numCourses)}

        for pre, course in prerequisites:
            graph[pre].append(course)

        return graph