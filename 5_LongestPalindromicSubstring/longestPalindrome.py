# 方法一： 马拉车算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'
        rl = [0 for _ in range(len(s))]
        pos, max_right = 0, 0
        ans = ''
        for i in range(len(s)):
            if i < max_right:
                rl[i] = min(rl[2 * pos - i], max_right - i)
            else:
                rl[i] = 1
            while 0 <= i - rl[i] and i + rl[i] < len(s) and s[i - rl[i]] == s[i + rl[i]]:
                rl[i] += 1
            if i + rl[i] - 1 > max_right:
                max_right = i + rl[i] - 1
                pos = i
            ans = max(ans, s[i-rl[i]+1:i+rl[i]], ans, key=len)
        return ans.replace('#', '')

# 方法二： dp
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[j][i] = dp[j + 1][i - 1] + 2
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j + 1][i])
        return dp[0][n - 1]
