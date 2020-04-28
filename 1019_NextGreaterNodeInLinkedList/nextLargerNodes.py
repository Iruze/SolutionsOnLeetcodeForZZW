# python3， 典型的单调栈解法

# 方法一： 两边扫描，链表转为列表在使用单调栈
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 将链表转化为列表
        def nodeToList(head):
            return [head.val] + nodeToList(head.next) if head else []
        
        l = nodeToList(head)
        ans = [0 for _ in range(len(l))]
        stack, i = [], 0
        # 单调栈：stack维护递减数列
        while i < len(l):
            while stack and l[stack[-1]] < l[i]:
                ans[stack.pop()] = l[i]
            stack.append(i)
            i += 1
        return ans



# 方法二：一遍扫描
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans = []
        stack = []
        i, node = 0, head
        # stack 维护单调递减序列，同时存储链表中节点位置
        while node:
            while stack and stack[-1][1] < node.val:
                tmp = stack.pop()
                ans[tmp[0]] = node.val
            stack.append((i, node.val))
            ans.append(0)
            i, node = i + 1, node.next
        return ans
