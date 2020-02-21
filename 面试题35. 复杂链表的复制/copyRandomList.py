"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        phead = head
        # copy
        while phead:
            thead = Node(phead.val)
            thead.next, phead.next = phead.next, thead
            phead = thead.next
        # copy random
        phead = head
        while phead:
            phead1 = phead.next
            if phead.random:
                phead1.random = phead.random.next
            phead = phead1.next
        # split
        res, phead = head.next, head
        while phead:
            phead1 = phead.next
            phead.next = phead1.next
            if phead1.next:
                phead1.next = phead1.next.next
            else:
                phead1.next = None
            phead = phead.next
        return res
