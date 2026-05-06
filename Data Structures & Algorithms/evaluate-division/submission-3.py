class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)

        result = []
        for (v1, v2) in queries:
            if v1 not in graph or v2 not in graph:
                result.append(-1)
            else:
                result.append(self.dfs(v1, v2, graph, 1, set([v1])))
        return result

        

    def build_graph(self, equations, values):
        # 使用嵌套字典：graph[v1] 返回一个字典，graph[v1][v2] 返回权重
        graph = collections.defaultdict(dict)
        
        for i in range(len(equations)):
            (v1, v2) = equations[i]
            value = values[i]
            graph[v1][v2] = value
            graph[v2][v1] = 1.0 / value
        return graph
    
    def dfs(self, v1, v2, graph, value, visited):
        if v2 in graph[v1]:
            return graph[v1][v2] * value

        for v_nxt in graph[v1]:
            if v_nxt in visited:
                continue
            
            result = self.dfs(
                v_nxt,
                v2,
                graph,
                value * graph[v1][v_nxt],
                visited | {v_nxt}
            )

            if result != -1:
                # cache optimization
                graph[v1][v2] = result / value
                graph[v2][v1] = value / result
                return result
        return -1        
