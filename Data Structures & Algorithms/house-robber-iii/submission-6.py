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
        return max(self.rob_max(root))

    def rob_max(self, root):
        # Base case: an empty subtree contributes nothing.
        if not root:
            return 0, 0
        
        left_rob, left_no_rob = self.rob_max(root.left)
        right_rob, right_no_rob = self.rob_max(root.right)

        root_rob = left_no_rob + right_no_rob + root.val
        root_no_rob = max(left_rob, left_no_rob) + max(right_rob, right_no_rob)
        return root_rob, root_no_rob