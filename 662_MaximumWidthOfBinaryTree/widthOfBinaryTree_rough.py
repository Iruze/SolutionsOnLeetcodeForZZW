# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        max_width = 0
        deque = collections.deque()
        deque.append(root)
        while deque:
            n = len(deque)
            max_width = max(max_width, n)
            for i in range(n):
                node = deque.popleft()
                if not node:
                    deque.extend([None, None])
                else:
                    deque.extend([node.left, node.right])
            self.__trimNone(deque)
        return max_width

    def __trimNone(self, deque):
        while deque and not deque[0]:
            deque.popleft()
        while deque and not deque[-1]:
            deque.pop()
    
