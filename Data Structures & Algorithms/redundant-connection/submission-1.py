class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parents = {i: i for i in range(1, len(edges) + 1)}
        self.sizes = {i: 1 for i in range(1, len(edges) + 1)}
        for (x, y) in edges:
            if not self.union(x, y):
                return [x, y]
        return [-1, -1]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False
        
        if self.sizes[x_root] >= self.sizes[y_root]:
            self.parents[y_root] = x_root
            self.sizes[x_root] += self.sizes[y_root]
        else:
            self.parents[x_root] = y_root
            self.sizes[y_root] += self.sizes[x_root]
        return True

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    