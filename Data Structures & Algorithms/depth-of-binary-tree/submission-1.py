# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.depth = 0
        self.traverse(root)
        return self.max_depth

    def traverse(self, root):
        if not root:
            return
        
        self.depth += 1
        self.traverse(root.left)
        # if this is a leaf
        if not root.left and not root.right:
            self.max_depth = max(self.depth, self.max_depth)
        self.traverse(root.right)
        self.depth -= 1





