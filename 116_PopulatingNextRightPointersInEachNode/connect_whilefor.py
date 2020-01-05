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
        if not root: return root
        deque = collections.deque()
        deque.append(root)
        while deque:
            n = len(deque)
            p = None
            for _ in range(n):
                tmp = deque.popleft()
                if p:
                    p.next = tmp
                    p = p.next
                else:
                    p = tmp
                if tmp.left:
                    deque.append(tmp.left)
                    deque.append(tmp.right)
            p.next = None
        return root
