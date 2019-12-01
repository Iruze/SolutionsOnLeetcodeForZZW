# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        slow = ListNode(0)
        slow.next, fast = head, head
        while fast:
            if fast.val != 9:
                slow = fast
            fast = fast.next
        slow.val += 1
        curr = slow.next
        while curr:
            curr.val = 0
            curr = curr.next
        return slow if slow.next == head else head
