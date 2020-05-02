class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
        # 初始化
        dp[0][0] = True
        # s为空，当前p中字符为'*'且，前面匹配true，则当前为true
        for i in range(1, lp + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
        # dp[i] 表示的是第i个字符，从1开始计
        # s[i - 1] 表示的对应的字符，从0开始计
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]
