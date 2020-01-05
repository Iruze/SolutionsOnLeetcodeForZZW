# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.__countLevel(root.left)
        right = self.__countLevel(root.right)
        if left == right:
            return self.countNodes(root.right) + (1 << left)
        else:
            return self.countNodes(root.left) + (1 << right)

    def __countLevel(self, root):
        level = 0
        while root:
            level += 1
            root = root.left
        return level
