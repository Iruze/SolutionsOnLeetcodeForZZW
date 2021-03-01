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
        """
        思路:
        中序遍历:  1234, 交换了1和4
        变成了:    4321
        那么, 第一个节点就是4, 第二个节点就是1, 找到first和second的节点后, 交换他们的"值"即可
        """

        self.firstnode = None
        self.secondnode = None
        self.prenode = TreeNode(float('-inf'))

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if not self.firstnode and self.prenode.val > root.val:
                self.firstnode = self.prenode
            if self.firstnode and self.prenode.val > root.val:
                self.secondnode = root
            self.prenode = root
            inorder(root.right)
        
        inorder(root)
        self.firstnode.val, self.secondnode.val = self.secondnode.val, self.firstnode.val
