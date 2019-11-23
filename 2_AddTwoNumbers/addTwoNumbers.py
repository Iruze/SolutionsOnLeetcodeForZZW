# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        curNode = ListNode(0)
        p, q, dummy = l1, l2, curNode
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            ssum = x + y + carry
            curNode.next = ListNode(ssum % 10)
            carry = ssum // 10
            
            curNode = curNode.next
            p = p.next if p else None
            q = q.next if q else None
        curNode.next = ListNode(1) if carry > 0 else None
        return dummy.next
