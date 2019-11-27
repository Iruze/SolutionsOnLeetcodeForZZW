# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        vhead = slow.next
        if not vhead: return head
        slow.next = None
        vhead = self.__reverseList(vhead)
        pNode1, pNode2 = head, vhead
        while pNode1 and pNode2:
            tmp1, tmp2 = pNode1.next, pNode2.next
            pNode1.next, pNode2.next = pNode2, tmp1
            pNode1, pNode2 = tmp1, tmp2
        return head

    def __reverseList(self, head):
        pre, pNode = None, head
        while pNode:
            pNode.next, pre, pNode = pre, pNode, pNode.next
        return pre
