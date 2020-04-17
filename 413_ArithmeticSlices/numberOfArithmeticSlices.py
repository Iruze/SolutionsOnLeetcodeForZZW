"""
双指针解法，每次记录下公差，如果确定了长度为l的等差数组，则其子等差数组个数的计算公式为: (l - 1) * (l - 2) / 2：
"""
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        ans = 0
        n = len(A)
        lo, hi = 0, 1
        while hi < n - 1:
            d = A[hi] - A[lo]
            while hi < n - 1 and A[hi + 1] - A[hi] == d:
                hi += 1
            # 如果lo, hi区间为等差数组
            if hi - 2 >= lo:
                l = hi - lo + 1
                # 长度确定为l的等差数组的子等差数组的个数计算公式
                ans += (l - 2) * (l - 1) // 2
            lo, hi = hi, hi + 1
        return ans
