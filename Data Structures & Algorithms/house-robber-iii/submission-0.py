# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.rob_max(root))
        
    def rob_max(self, root):
        if not root:
            return 0, 0

        left_rob_max, left_no_rob_max = self.rob_max(root.left)
        right_rob_max, right_no_rob_max = self.rob_max(root.right)

        cur_rob_max = root.val + left_no_rob_max + right_no_rob_max
        cur_no_rob_max = max(left_rob_max, left_no_rob_max) + max(right_rob_max, right_no_rob_max)

        return cur_rob_max, cur_no_rob_max