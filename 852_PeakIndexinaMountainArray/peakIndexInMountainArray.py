# 方法一： 线性扫描 O(n)

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                return i
        return -1

# 方法二： 二分法 O(logn)
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            # 不是 lo, mid, hi 的比较，而是mid, mid + 1的比较
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
