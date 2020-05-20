# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def helper(root, pre=0):
            if not root: return 0
            cur = pre * 10 + root.val
            if not root.left and not root.right: return cur
            return helper(root.left, cur) + helper(root.right, cur)
        
        return helper(root)
