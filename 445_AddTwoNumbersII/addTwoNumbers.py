# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1, str2 = '', ''
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        str3, carry = '', 0
        i1, i2 = len(str1) - 1, len(str2) - 1
        while i1 >= 0 or i2 >= 0:
            v1 = int(str1[i1]) if i1 >= 0 else 0
            v2 = int(str2[i2]) if i2 >= 0 else 0
            ssum = v1 + v2 + carry
            carry = ssum // 10
            str3 = str(ssum % 10) + str3
            i1, i2 = i1 - 1, i2 - 1
        if carry > 0:
            str3 = '1' + str3
        dummy = ListNode(-1)
        pNode = dummy
        for s3 in str3:
            pNode.next = ListNode(int(s3))
            pNode = pNode.next
        pNode.next = None
        return dummy.next
