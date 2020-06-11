class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p: return 0
        from collections import defaultdict
        dp = defaultdict(int)
        dp[p[0]] = 1
        curMaxLen = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                curMaxLen += 1
            else:
                curMaxLen = 1
            dp[p[i]] = max(dp[p[i]], curMaxLen)
        return sum(dp.values())
