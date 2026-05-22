class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}
        for (x, y) in edges:
            self.union(x, y)
        
        roots = set()
        for i in range(n):
            roots.add(self.find(i))
        return len(roots)

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.size[x_root] > self.size[y_root]:
            self.parents[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        else:
            self.parents[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        