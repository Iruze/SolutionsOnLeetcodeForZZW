# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        cur_nodes = deque()
        cur_nodes.append(root)
        flag = True
        while cur_nodes:
            nex_nodes = deque()
            cur_val = deque()
            for nd in cur_nodes:
                if nd:
                    if flag: cur_val.append(nd.val)
                    else: cur_val.appendleft(nd.val)
                    nex_nodes.extend([nd.left, nd.right])
            if cur_val:
                output.append(list(cur_val))
            flag = not flag
            cur_nodes = nex_nodes
        return output
