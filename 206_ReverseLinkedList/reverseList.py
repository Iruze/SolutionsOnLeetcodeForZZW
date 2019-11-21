# ###################################################### 
#               solution1: 递归解法
# ###################################################### 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
 
 
 
# ###################################################### 
#               solution2: 迭代解法
# ###################################################### 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre
