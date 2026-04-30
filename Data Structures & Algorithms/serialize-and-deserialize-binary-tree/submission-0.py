# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        queue = collections.deque([root])
        result = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    result.append('#')
                else:
                    result.append(str(node.val))
                if node:
                    queue.append(node.left)
                if node:
                    queue.append(node.right)
        
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data_l = data.split(',')
        root = TreeNode(data_l[0])
        queue = collections.deque([root])
        i = 0
        while queue:
            node = queue.popleft()
            left, right = data_l[i + 1], data_l[i + 2]
            if left != '#':
                node.left = TreeNode(left)
                queue.append(node.left)
            if right != '#':
                node.right = TreeNode(right)
                queue.append(node.right)
            i += 2
        return root


