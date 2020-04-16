"""
如果链表有 NN 个结点，则分隔的链表中每个部分中都有 n/kn/k 个结点，且前 N\%kN%k 部分有一个额外的结点。我们可以用一个简单的循环来计算 NN。
现在对于每个部分，我们已经计算出该部分有多少个节点：width + (i < remainder ? 1 : 0)。直接拆分原链表，并根据需要返回指向原始链表中节点的指针列表。


"""
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        N = 0
        while cur:
            cur = cur.next
            N += 1
        width, reminder = divmod(N, k)
        cur = root
        ans = []
        for i in range(k):
            head = cur
            for j in range(width + (i < reminder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans
        
