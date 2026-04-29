# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.get_depth(root)
        return self.is_balanced
    
    def get_depth(self, root):
        if not root:
            return 0
        
        left_h = self.get_depth(root.left)
        right_h = self.get_depth(root.right)
        if abs(left_h - right_h) > 1:
            self.is_balanced = False
        return 1 + max(left_h, right_h)
