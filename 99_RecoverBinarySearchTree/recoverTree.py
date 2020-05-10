# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.preNode = TreeNode(float('-Inf'))
        self.firstNode = None
        self.secondNode = None

        def inorder(root):
            if not root: return
            inorder(root.left)
            # 左子树上第一个错误节点是大于root的节点
            if not self.firstNode and self.preNode.val >= root.val:
                self.firstNode = self.preNode
            # 左子树上第二个错误节点是root的节点(如果存在的话)
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            inorder(root.right)

        inorder(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val        
