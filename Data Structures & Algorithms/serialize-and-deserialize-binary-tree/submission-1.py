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
        res = [str(root.val)]
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
                res.append(str(cur.left.val))
            else:
                res.append('#')

            if cur.right:
                queue.append(cur.right)
                res.append(str(cur.right.val))
            else:
                res.append('#')
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data_l = data.split(',')
        root = TreeNode(data_l[0])
        queue = collections.deque([root])
        i = 0
        while queue:
            cur = queue.popleft()
            if data_l[i + 1] != '#':
                cur.left = TreeNode(int(data_l[i + 1]))
                queue.append(cur.left)
            if data_l[i + 2] != '#':
                cur.right = TreeNode(int(data_l[i + 2]))
                queue.append(cur.right)
            i += 2

        return root
