# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        length, pNode = 0, head
        while pNode:
            length += 1
            pNode = pNode.next
        if k > length or length == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        res = None
        for i in range(length // k):
            _, dummy = self.__reverseMN(dummy, 2, 1 + k)
            if i == 0:
                res = _.next
        return res

    def __reverseMN(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next, pre = head, dummy
        for _ in range(1, m):
            pre = pre.next
        pLeft, front, pNode = pre, pre.next, pre.next
        for _ in range(m, n + 1):
            pNode.next, pre, pNode = pre, pNode, pNode.next
        tail, pRight = pre, pNode
        pLeft.next, front.next = tail, pRight
        return dummy.next, front
