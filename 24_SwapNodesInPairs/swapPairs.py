class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # # solution1: 递归版本
        # if not head or not head.next:
        #     return head
        # dummy = head.next
        # head.next, dummy.next = dummy.next, head
        # dummy.next.next = self.swapPairs(head.next)
        # return dummy

        # solution3: 迭代版本

        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, dummy.next
        while cur and cur.next:
            tmp = cur.next.next
            pre.next = cur.next
            cur.next.next = cur
            cur.next = tmp
            pre, cur = cur, cur.next
        return dummy.next
