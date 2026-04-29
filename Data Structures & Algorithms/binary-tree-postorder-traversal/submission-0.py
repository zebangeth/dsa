# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.traverse(root)
        return self.result

    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.left)
        self.traverse(root.right)
        self.result.append(root.val)