class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        pre, cur = head, head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head
