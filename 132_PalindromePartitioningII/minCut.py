import functools


class Solution:
    @functools.lru_cache(None)
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        ans = float('Inf')
        for i in range(1, len(s) + 1):
            # 划分的第一个字符是回文串的情况
            if s[:i] == s[:i][::-1]:
                ans = min(ans, self.minCut(s[i:]) + 1)
        return ans
