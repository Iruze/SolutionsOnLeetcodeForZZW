# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        rhead = None
        for l in lists:
            rhead = self.__mergeTwoLists(rhead, l)
        return rhead
    
    def __mergeTwoLists(self, head1, head2):
        dummy = ListNode(-1)
        pNode = dummy
        while head1 and head2:
            if head1.val < head2.val:
                pNode.next = head1
                head1 = head1.next
            else:
                pNode.next = head2
                head2 = head2.next
            pNode = pNode.next
        pNode.next = head1 if head1 else head2
        return dummy.next
