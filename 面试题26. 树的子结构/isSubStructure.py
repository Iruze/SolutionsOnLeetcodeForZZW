# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def sameroot(A, B):
            if not B: return True
            if not A: return not B 
            return A.val == B.val and sameroot(A.left, B.left) and sameroot(A.right, B.right)
        if not B: return False
        if not A: return not B
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B) or sameroot(A, B)
