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
        data = [str(root.val)]
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    data.append(str(cur.left.val))
                else:
                    data.append('#')
                if cur.right:
                    queue.append(cur.right)
                    data.append(str(cur.right.val))
                else:
                    data.append('#')
        return ",".join(data)
                
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        data_l = collections.deque(data.split(','))
        root_val = data_l.popleft()
        root = TreeNode(int(root_val))
        queue = collections.deque([root])
        while data_l:
            cur = queue.popleft()
            left = data_l.popleft()
            right = data_l.popleft()
            if left != '#':
                cur.left = TreeNode(int(left))
                queue.append(cur.left)
            if right != '#':
                cur.right = TreeNode(int(right))
                queue.append(cur.right)
        return root

