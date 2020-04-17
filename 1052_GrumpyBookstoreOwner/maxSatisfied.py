"""
复杂度O(n)， 滑动窗口解法；

先计算没有X维持的时候的满意数
在计算有X时候的补偿值 结果=1 + 2
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        # 计算没有X维持的时候的满意数
        ans = sum(map(lambda x,y: (1-x)*y, grumpy, customers))
        # compensate: 在有X时候的满意数的最大补偿值
        # window: X窗口内的满意数的补偿值
        compensate, window = 0, 0
        lo, hi = 0, 0
        while hi < n:
            window += grumpy[hi] * customers[hi]
            # 维护大小为X的窗口，计算窗口内的补偿值
            while hi - lo + 1 > X:
                window -= grumpy[lo] * customers[lo]
                lo += 1
            compensate = max(compensate, window)
            hi += 1
        return ans + compensate
