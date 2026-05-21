# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_valid(root, float('inf'), -float('inf'))
        
    def check_valid(self, node, upper_bound, lower_bound):
        if not node:
            return True
        if not lower_bound < node.val < upper_bound:
            return False
        
        left_valid = self.check_valid(node.left, node.val, lower_bound)
        right_valide = self.check_valid(node.right, upper_bound, node.val)
        return left_valid and right_valide