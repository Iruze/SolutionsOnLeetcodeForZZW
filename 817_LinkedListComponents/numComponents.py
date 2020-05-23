# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # G中可能存在重复的元素，在链表上扫描时如果有该整型值，其个数要对应-1
        from collections import Counter
        G = Counter(G)

        ans = 0
        # pre用来记录前一个是否也在G中，即当前是否连续
        pre = False
        while head:
            if head.val not in G:
                pre = False
            else:
                # G[head.val] <= 0说明head.val在前面的扫描中已经对应分配完了
                if not pre or G[head.val] <= 0:
                    ans += 1
                    pre = True
                # 可能G[head.val] < 0
                G[head.val] -= 1
            head = head.next
        return ans
