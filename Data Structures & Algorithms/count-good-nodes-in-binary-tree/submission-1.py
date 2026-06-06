# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.count_good(root, -float('inf'))
        return self.count
    
    def count_good(self, root, path_max):
        if not root:
            return 0
        
        if root.val >= path_max:
            self.count += 1
        
        path_max = max(path_max, root.val)
        self.count_good(root.left, path_max)
        self.count_good(root.right, path_max)

        