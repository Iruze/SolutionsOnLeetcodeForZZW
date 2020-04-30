# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def longestConsecutive(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root):
            if not root: return 0
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1
            if root.left and root.val + 1 != root.left.val:
                # 将左子树抽象想象为一个节点
                l = 1
            if root.right and root.val + 1 != root.right.val:
                # 同理，将右子树抽象想象为一个节点
                r = 1
            cur = max(l, r)
            self.ans = max(self.ans, cur)
            return cur
        dfs(root)
        return self.ans
