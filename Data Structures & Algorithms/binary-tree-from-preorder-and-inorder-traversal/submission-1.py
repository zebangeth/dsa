# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        inorder_root_val_index = inorder.index(root_val)
        
        if inorder_root_val_index == 0:
            left_in, left_pre = [], []
        else: 
            left_in = inorder[:inorder_root_val_index]
            left_pre = preorder[1:len(left_in) + 1]
        
        if inorder_root_val_index == len(inorder) - 1:
            right_in, right_pre = [], []
        else: 
            right_in = inorder[inorder_root_val_index + 1:]
            right_pre = preorder[inorder_root_val_index + 1:]

        left_sub = self.buildTree(left_pre, left_in)
        right_sub = self.buildTree(right_pre, right_in)
        return TreeNode(root_val, left_sub, right_sub)
