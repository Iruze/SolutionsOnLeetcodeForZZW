# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ''
        
        res = '' + str(t.val)
        if not t.left and not t.right: return res
        
        left = '(' + self.tree2str(t.left) + ')' if t.left else '()'
        right = '(' + self.tree2str(t.right) + ')' if t.right else ''
        
        return res + left + right
