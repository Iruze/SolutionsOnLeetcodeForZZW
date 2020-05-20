# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        ans = []
        for x in range(N):
            # 去掉根节点的1
            y = N - 1 - x
            # 每一个左右子树同样是满二叉树，结果是所有左右子树的排列组合
            for left in self.allPossibleFBT(x):
                for right in self.allPossibleFBT(y):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)
        return ans
