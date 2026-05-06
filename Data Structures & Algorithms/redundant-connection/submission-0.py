class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)
        
        for n1, n2 in edges: 
            if not self._union(n1, n2, parents, size): 
                return [n1, n2]

    def _find(self, node, parents):
        if node != parents[node]:
            # 添加路径压缩的功能，parents 直接更改为指向根节点，这样可以提高并查集的效率
            parents[node] = self._find(parents[node], parents)
        return parents[node]
    
    def _union(self, n1, n2, parents, size):
        root1 = self._find(n1, parents)
        root2 = self._find(n2, parents)
        
        if root1 == root2:
            return False
        
        if size[root2] > size[root1]:
            root1, root2 = root2, root1
        
        parents[root2] = root1
        size[root1] += size[root2]
        return True
        
