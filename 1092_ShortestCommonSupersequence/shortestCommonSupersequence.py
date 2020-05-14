class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 求出最长公共子序列lcs
        n1, n2 = len(str1), len(str2)
        dp = [['' for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                elif len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
        
        # 不在lcs中的字符都要加入到scs
        lcs = dp[-1][-1]
        i1, i2 = 0, 0
        ans = ''
        for c in lcs:
            while i1 < n1 and str1[i1] != c:
                ans += str1[i1]
                i1 += 1
            while i2 < n2 and str2[i2] != c:
                ans += str2[i2]
                i2 += 1
            ans += c
            i1 += 1
            i2 += 1
        return ans + str1[i1:] + str2[i2:]
