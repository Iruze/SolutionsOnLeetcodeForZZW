# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        val = postorder[-1]
        root = TreeNode(val)
        idx = inorder.index(val)
        
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right= self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return root
