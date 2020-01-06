"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        deque = collections.deque()
        deque.append(root)
        while deque:
            n = len(deque)
            for _ in range(n):
                node = deque.popleft()
                if _ == n - 1:
                    node.next = None
                else:
                    node.next = deque[0]
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
        return root
