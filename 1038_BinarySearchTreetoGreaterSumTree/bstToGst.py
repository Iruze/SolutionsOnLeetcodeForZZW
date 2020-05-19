"""
python3, 右中左，遍历累加，比较简单，直接看代码：
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.pre = 0

        # 右，中，左 遍历累加
        def dfs(root):
            if not root: return
            dfs(root.right)
            root.val += self.pre
            self.pre = root.val
            dfs(root.left)
        
        dfs(root)
        return root
