class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        lo, hi = 0, 0           # lo, hi用来记录当前'('和')'的数量
        ans = 0
        for s in S:
            if s == '(':
                lo += 1
            else:
                hi += 1
            if lo < hi:         # ')'的数量大于'('的数量，一定是无效的，需要添加'('
                ans += hi - lo  # 添加的'('数量为hi与lo之差
                lo = hi         # 添加'('之后，两者数量相等
        ans += abs(lo - hi)     # S全部扫描完之后，需要再次清点lo和hi之差
        return ans
