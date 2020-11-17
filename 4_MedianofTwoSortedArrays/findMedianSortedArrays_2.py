class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1) // 2
        # 下标: 0 1 2 3 4 5 6 (7)
        # n1+n2为奇(7): k=4，在中位数3偏右
        # n1+n2为偶(8): k=4, 在中位数3,4,偏右
        # 综上，下标k是中位数下标偏右，这样就可以复用c1, 偶数的时候只需要计算出c2
        lo, hi = 0, n1
        while lo < hi:
            i = lo + ((hi - lo) >> 1)
            j = k - i
            if nums1[i] < nums2[j - 1]:
                lo = i + 1
            else:
                hi = i
        i, j = lo, k - lo
        # nums1, nums2可能到数组头
        c1 = max(nums1[i - 1] if i > 0 else float('-Inf'), nums2[j - 1] if j > 0 else float('-Inf'))
        if (n1 + n2) & 1:
            return c1
        # nums1, nums2可能到数组尾
        c2 = min(nums1[i] if i < n1 else float('Inf'), nums2[j] if j < n2 else float('Inf'))
        return (c1 + c2) / 2.0
