# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        deque = collections.deque()
        deque.append((1, root))
        i = 0
        while i < len(deque):
            pos, node = deque[i]
            i += 1
            if node:
                deque.append((pos * 2, node.left))
                deque.append((pos * 2 + 1, node.right))

        return deque[-1][0] == len(deque)
