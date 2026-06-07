# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path_max = -float('inf')
        self.get_branch_max(root)
        return self.path_max
    
    def get_branch_max(self, root):
        if not root:
            return 0

        left_branch_max = self.get_branch_max(root.left)
        right_branch_max = self.get_branch_max(root.right)
        path = max(left_branch_max, 0) + root.val + max(right_branch_max, 0)
        branch = root.val + max(left_branch_max, right_branch_max, 0)
        self.path_max = max(self.path_max, path, branch)
        return branch
