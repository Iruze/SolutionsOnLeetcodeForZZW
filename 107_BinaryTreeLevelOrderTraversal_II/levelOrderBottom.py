# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        output = []
        cur_nodes = deque()
        cur_nodes.append(root)
        while cur_nodes:
            nex_nodes = deque()
            cur_val = []
            for nd in cur_nodes:
                if nd:
                    cur_val.append(nd.val)
                    nex_nodes.extend([nd.left, nd.right])
            if cur_val:
                output.insert(0, cur_val)
            cur_nodes = nex_nodes
        return output
