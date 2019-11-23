# ############################################################
#               solution1: 递归解法
# ############################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        res = None
        if l1.val < l2.val:
            res = l1
            res.next = self.mergeTwoLists(l1.next, l2)
        else:
            res = l2
            res.next = self.mergeTwoLists(l1, l2.next)
        return res

# ############################################################
#               solution2: 迭代解法
# ############################################################
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pNode = dummy
        while l1 and l2:
            if l1.val < l2.val:
                pNode.next = l1
                l1 = l1.next
            else:
                pNode.next = l2
                l2 = l2.next
            pNode = pNode.next
        pNode.next = l1 if l1 else l2
        return dummy.next
