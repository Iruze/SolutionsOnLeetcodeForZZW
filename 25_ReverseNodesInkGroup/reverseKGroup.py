# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 解法一
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

    
# 解法二
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         if not head or not head.next:
#             return head
#         dummy = ListNode(-1)
#         dummy.next = head
#         last = self._reverseK(dummy, k)
#         # _reverseK()返回已翻转的长度为k的链表的最后一个节点
#         while last:
#             last = self._reverseK(last, k)
#         return dummy.next
    
    
#     def _reverseK(self, dummy, k):
#         """"
#         将dummy.next开头的长度为k的链表翻转，并且衔接好翻转后的左右的断点
#         """
#         l1, l2 = dummy, dummy.next
#         pre, cur, end = dummy, dummy.next, dummy.next
#         for _ in range(k):
#             # 当前片段长度小于k， 提前结束，返回None
#             if not end:
#                 return None
#             end = end.next
#         while cur != end:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         # 衔接好断点, pre, cur为右断点处的两点(r1, r2)
#         l1.next, l2.next = pre, cur
#         return l2
