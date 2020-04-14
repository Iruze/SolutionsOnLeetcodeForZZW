"""
dp[i][0]，dp[i][1] 分别代表字符 S[i] 最终选择 0 和 1 的最少翻转次数，
考虑到递增，那么 dp[i][0] 只能由 dp[i-1][0] 转化而来，所以，状态转移方程如下：

如果 S[i] 是 '1':
dp[i][0] = dp[i-1][0] + 1 # 只能从 0 转化来，翻转 '1' 为 '0'，翻转次数加 1
dp[i][1] = min(dp[i-1][0], dp[i-1][1]) # 已经为 '1'，无需翻转

如果 S[i] 是 '0':
dp[i][0] = dp[i-1][0] # 只能从 0 转化来，无需翻转
dp[i][1] = min(dp[i-1][0] + 1, dp[i-1][1] + 1) # 翻转 '0' 为 '1'，翻转次数加 1
"""

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        zeros, ones = 0, 0
        for s0 in S:
            if s0 == '0':
                ones = min(ones, zeros) + 1
            else:
                zeros, ones = zeros + 1, min(zeros, ones)
        return min(zeros, ones)
