"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def _dfs(node):
            if not node:
                return
            for ch in node.children:
                _dfs(ch)
            self.res.append(node.val)
        self.res = []
        _dfs(root)
        return self.res
