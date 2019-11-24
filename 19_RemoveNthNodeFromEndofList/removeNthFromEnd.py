# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pNode1, pNode2 = dummy, dummy
        while n:
            pNode2 = pNode2.next
            n -= 1
        while pNode2 and pNode2.next:
            pNode1, pNode2 = pNode1.next, pNode2.next
        pNode1.next = pNode1.next.next
        return dummy.next
