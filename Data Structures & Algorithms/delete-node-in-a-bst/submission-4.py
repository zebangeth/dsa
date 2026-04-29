class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            right_min_leaf = self._min_leaf(root.right)
            right_min_leaf.left = root.left
            return root.right
        
        return root


    # find and return the smallest/mostleft node in a binary tree
    def _min_leaf(self, node):
        while node.left:
            node = node.left
        return node