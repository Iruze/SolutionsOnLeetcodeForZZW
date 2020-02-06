# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # 求链表中点的前一个节点，和中点
        pre, mid = self.__mid(head)
        pre.next = None
        root = TreeNode(mid.val)
        # 新二叉树左子树递归
        root.left = self.sortedListToBST(head)
        # 新二叉树右子树递归
        root.right = self.sortedListToBST(mid.next)
        return root

    def __mid(self, head):
        pre = ListNode(-1)
        pre.next = head
        pnode = head
        # 快慢指针求得链表中点
        while pnode and pnode.next:
            pnode = pnode.next.next
            pre = pre.next
        # 返回链表中点前一个节点、中点
        return pre, pre.next
