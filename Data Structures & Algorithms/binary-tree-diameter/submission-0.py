# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.longest_path = 0
        self.get_depth(root)
        return self.longest_path
    
    def get_depth(self, root):
        if not root:
            return 0

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        self.longest_path = max(self.longest_path, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)