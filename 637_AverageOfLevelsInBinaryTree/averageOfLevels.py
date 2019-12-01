# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import numpy as np
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        cur, nxt = deque(), deque()
        output = list()
        cur.append(root)
        while cur or nxt:
            output.append(np.mean([x.val for x in cur]))
            while cur:
                t = cur.popleft()
                if t.left: nxt.append(t.left)
                if t.right: nxt.append(t.right)
            cur, nxt = nxt, deque()
        return output
