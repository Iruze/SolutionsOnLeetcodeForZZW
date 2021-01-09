class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)                     # 分别先展开左, 右子树
        self.flatten(root.right)
        tmp = root.right                            # 保留右子树
        root.left, root.right = None, root.left     # 左子树当右子树, 然后左子树置空
        while root.right:
            root = root.right                       # 遍历到右子树末尾
        root.right = tmp                            # 末尾续结上保留的右子树
