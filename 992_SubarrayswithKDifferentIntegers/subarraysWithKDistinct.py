class Solution:
    """
    1). 维护不同元素个数作为K的窗口；
    2). 当恰好为K个不同元素时， 尝试移动窗口左端，边移动边计算；
    3). 当2)不满足大小为K的窗口时，恢复2)移动左端前的状态
    """
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window = collections.defaultdict(int)
        ans = 0
        cur = 0
        lo, hi = 0, 0
        while hi < len(A):
            if window[A[hi]] == 0: cur += 1
            window[A[hi]] += 1
            # keep the window with K different num
            while cur > K:
                window[A[lo]] -= 1
                if window[A[lo]] == 0: cur -= 1
                lo += 1
            if cur == K:
                t = lo
                # try to move the left boundary
                while cur == K:
                    # calculate the result
                    ans += 1
                    window[A[t]] -= 1
                    if window[A[t]] == 0: cur -= 1
                    t += 1
                # recover the left boundary
                for j in range(lo, t):
                    if window[A[j]] == 0: cur += 1
                    window[A[j]] += 1
            hi += 1
        return ans
