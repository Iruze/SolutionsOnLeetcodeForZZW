class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        lo, hi = 0, n - 1
        # lo尽可能靠近数组开头，这样得到的h最大
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if n - mid > citations[mid]:
                lo = mid + 1
            else:
                hi = mid
        # 当[0, 0]这样的 n - lo = 2, 实际上h应该为0
        return n - lo if citations[lo] != 0 else 0
