# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def match(head, root):
            if not head: return True
            if not root: return False
            if root.val != head.val: return False
            return match(head.next, root.left) or match(head.next, root.right)
        if not head: return True
        if not root: return False
        if match(head, root): return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
