# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tilt = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.__travel(root)
        return self.tilt

    def __travel(self, root):
        if not root: return 0
        left = self.__travel(root.left)
        right = self.__travel(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val
