# #################################################
#             Solution1: 迭代解法
# #################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next, pre = head, dummy
        for i in range(1, m):
            pre = pre.next
        pLeft, front, pNode = pre, pre.next, pre.next
        for i in range(m, n + 1):
            pNode.next, pre, pNode = pre, pNode, pNode.next
        pRight, tail = pNode, pre
        pLeft.next, front.next = tail, pRight
        return dummy.next
 
 
# #################################################
#             Solution2: 递归解法
# #################################################
class Solution:
    successor = None
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        else:
            head.next = self.reverseBetween(head.next, m - 1, n - 1)
            return head
    
    
    def reverseN(self, head, n):
        global successor
        if n == 1:
            successor = head.next
            return head
        else:
            last = self.reverseN(head.next, n - 1)
            head.next.next, head.next = head, successor
            return last
