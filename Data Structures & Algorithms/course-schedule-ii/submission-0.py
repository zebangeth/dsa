class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees, graph = self.build_graph(numCourses, prerequisites)

        starts = []
        for course in indegrees:
            if indegrees[course] == 0:
                starts.append(course)
        
        sequence = starts[:]
        queue = collections.deque(starts)
        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    queue.append(nxt)
                    sequence.append(nxt)
        
        return sequence if len(sequence) == numCourses else []

    
    def build_graph(self, numCourses, prerequisites):
        indegrees = {course: 0 for course in range(numCourses)}
        graph = collections.defaultdict(list)
        for nxt, pre in prerequisites:
            indegrees[nxt] += 1
            graph[pre].append(nxt)
        return indegrees, graph