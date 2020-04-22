# bfs层次搜索
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        cur, nxt = [], []
        cur.append(root)
        while cur:
            tmp = []
            for node in cur:
                if node:
                    tmp.append(node.val)
                    nxt += node.children
            ans.append(tmp)
            cur, nxt = nxt, []
        return ans
