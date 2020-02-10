class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        asc1 = 0
        for i in range(1, n1 + 1):
            asc2 = 0
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                asc2 += ord(s2[j - 1])
            asc1 += ord(s1[i - 1])
        return asc1 + asc2 - 2 * dp[-1][-1]
