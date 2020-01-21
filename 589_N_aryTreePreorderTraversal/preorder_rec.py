"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def _dfs(node):
            if node:
                self.res.append(node.val)
                for ch in node.children:
                    _dfs(ch)
        self.res = []
        _dfs(root)
        return self.res
