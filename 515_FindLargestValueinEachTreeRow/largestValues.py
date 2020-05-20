# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        ans = []
        cur, nxt = [root], []
        while cur:
            maxv = -float('Inf')
            for node in cur:
                maxv = max(maxv, node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            ans.append(maxv)
            cur, nxt = nxt, []
        return ans
