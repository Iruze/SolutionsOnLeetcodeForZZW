# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        fast = slow.next
        slow.next = None
        slow = dummy.next
        pre = None
        while fast:
            fast.next, fast, pre = pre, fast.next, fast
        while pre:
            if pre.val != slow.val: return False
            slow, pre = slow.next, pre.next
        return True
