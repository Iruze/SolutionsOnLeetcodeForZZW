# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(root):
            if not root: return None
            if root.val > R: return trim(root.left)
            if root.val < L: return trim(root.right)
            root.left = trim(root.left)
            root.right = trim(root.right)
            return root
        return trim(root)
