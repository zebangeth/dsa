class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees, graph = self.build_graph(numCourses, prerequisites)

        starts = []
        for course, indegree in indegrees.items():
            if indegree == 0:
                starts.append(course)

        queue = collections.deque(starts)
        taken = 0
        while queue:
            cur = queue.popleft()
            taken += 1
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    queue.append(nxt)
        
        return taken == numCourses

    def build_graph(self, numCourses, prerequisites):
        indegrees = {course: 0 for course in range(numCourses)}
        graph = collections.defaultdict(list)

        for nxt, pre in prerequisites:
            indegrees[nxt] += 1
            graph[pre].append(nxt)
        
        return indegrees, graph
        