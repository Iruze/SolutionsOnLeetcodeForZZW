# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def _dfs(root, sum):
            if not root: return
            cur.append(root.val)
            if not root.left and not root.right and root.val == sum:
                output.append(cur[:])
            _dfs(root.left, sum - root.val)
            _dfs(root.right, sum - root.val)
            cur.pop()
        cur, output = [], []
        _dfs(root, sum)
        return output
