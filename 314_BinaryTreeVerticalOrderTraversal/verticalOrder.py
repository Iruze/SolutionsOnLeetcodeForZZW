# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        lockup = collections.defaultdict(list)
        def dfs(root, depth, loc):
            if not root: return
            lockup[loc].append([depth, root.val])
            dfs(root.left, depth + 1, loc - 1)
            dfs(root.right, depth + 1, loc + 1)
        
        dfs(root, 0, 0)
        return [[b for a, b in sorted(v, key=lambda x: x[0])] for k, v in sorted(lockup.items())]
