class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 二分法，选择 max(piles) 作为right的最大
        # 1 是最小的left
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            h1 = sum(math.ceil(p / mid) for p in piles)
            # h1 = H 有可能是 [4, 5] 两个同时满足 h1 = sum()
            # 所以，此时认为 h1 是比实际的 mid 大的值
            if h1 <= H:
                hi = mid
            else:
                lo = mid + 1
        return lo
