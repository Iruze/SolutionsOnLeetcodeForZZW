class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        # 这里定义dp的时候容易出错，是n2列，n1行
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        # 从1开始循环
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 这里切记i,j同时回退1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 维持前一个结果的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return n1 + n2 - dp[-1][-1] * 2
