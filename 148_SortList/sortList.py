# #####################################################
#               solution1: 递归解法
# #####################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        end = head
        while end.next:
            end = end.next
        return self.__mergeSort(head, end)
    
    def __mergeSort(self, head, end):
        if head == end: return head
        mid, midfast = head, head
        
        # 不能是: midfast != null && midfast.next != null
        # 因为存在 head.next = end 的情况不符合
        # 所以直接终点认为是 end，直接直接使得 中点mid 偏向头节点
        # 对于 midfast = midfast.next.next 的连续前进两步的必须要满足：
        # midfast != end and midfast.next != end， 否则while不能结束，报错stackoverflow.
        while midfast != end and midfast.next != end:
            mid, midfast = mid.next, midfast.next.next
        
        vhead, mid.next = mid.next, None
        head1 = self.__mergeSort(head, mid)
        head2 = self.__mergeSort(vhead, end)
        
        return self.__merge(head1, head2)
    
    def __merge(self, head1, head2):
        if not head1: return head2
        if not head2: return head1
        
        res = None
        if head1.val < head2.val:
            res = head1
            res.next = self.__merge(head1.next, head2)
        else:
            res = head2
            res.next = self.__merge(head1, head2.next)
        return res
