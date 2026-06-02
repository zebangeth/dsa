# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the max amount rob for a given root equals to:
# max(rob root, not rob root)
# rob root = (not rob left + not rob right)
# not rob root = max(not rob left, rob left) + max(not rob right, rob right)

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        root_rob, not_root_rob = self.rob_helper(root)
        return max(root_rob, not_root_rob)
        
    def rob_helper(self, root):
        if not root:
            return 0, 0
        
        left, not_left = self.rob_helper(root.left)
        right, not_right = self.rob_helper(root.right)

        root_rob = root.val + not_left + not_right
        not_root_rob = max(left, not_left) + max(right, not_right)
        return root_rob, not_root_rob