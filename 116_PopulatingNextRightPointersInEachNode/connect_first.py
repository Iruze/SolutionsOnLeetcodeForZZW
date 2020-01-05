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
        lay, curlayer = 1, 1
        while deque:
            node = deque.popleft()
            curlayer -= 1
            if node.left:
                deque.append(node.left)
                deque.append(node.right)
            if curlayer == 0:
                node.next = None
                curlayer = 1 << lay
                lay += 1
            else:
                node.next = deque[0]
        return root
