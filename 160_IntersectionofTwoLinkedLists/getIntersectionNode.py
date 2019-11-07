# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA, nodeB = headA, headB
        while True:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
