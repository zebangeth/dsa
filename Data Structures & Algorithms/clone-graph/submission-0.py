"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # clone node
        old_to_new = dict()
        self.clone_node(node, old_to_new)

        # clone edge
        self.clone_edge(old_to_new)
        return old_to_new[node]
    
    def clone_node(self, node, old_to_new):
        queue = collections.deque([node])
        old_to_new[node] = Node(node.val)
        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei in old_to_new:
                    continue
                old_to_new[nei] = Node(nei.val)
                queue.append(nei)
        return
    
    def clone_edge(self, old_to_new):
        for node in old_to_new:
            for nei in node.neighbors:
                old_to_new[node].neighbors.append(old_to_new[nei])
        return
