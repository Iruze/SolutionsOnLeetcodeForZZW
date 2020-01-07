# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        deque = collections.deque()
        deque.append((root, 1))
        res = 0
        while deque:
            res = max(res, deque[-1][1] - deque[0][1] + 1)
            for _ in range(len(deque)):
                node, pos = deque.popleft()
                if node.left:
                    deque.append((node.left, 2 * pos))
                if node.right:
                    deque.append((node.right, 2 * pos + 1))
        return res
    
