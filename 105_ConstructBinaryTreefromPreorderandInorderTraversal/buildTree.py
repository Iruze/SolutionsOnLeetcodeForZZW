# 解法一： 递归解法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder.pop(0))
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[:i], inorder[:i])
        root.right = self.buildTree(preorder[i:], inorder[i+1:])
        return root
