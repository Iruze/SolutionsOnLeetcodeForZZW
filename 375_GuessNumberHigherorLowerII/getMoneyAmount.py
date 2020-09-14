class Solution:
    def getMoneyAmount(self, n: int) -> int:

        # # 方法一: 记忆化递归
        # from functools import lru_cache

        # @lru_cache(None)
        # def helper(l, r):
        #     if r - l <= 0: return 0
        #     if r - l == 1: return l
        #     if r - l == 2: return l + 1
        #      """
        #      从(r, (r + l) / 2)内选择数字作为第一次尝试, 右边区间都比左边区间大,开销肯定大于左边, 总体开销也较大
        #      所以, 从((l + r) / 2, r)内选择, 这样两个区间的开销更接近, 且总体开销会更小
        #      """
        #     return min(x + max(helper(l, x - 1), helper(x + 1, r)) for x in range((l + r) >> 1, r))
        # return helper(1, n)

        # 方法二: dp方法, 将上述递归改为dp
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            dp[i][i + 1] = i
        for l in range(n + 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(x + max(dp[l][x - 1], dp[x + 1][r]) for x in range((l + r) >> 1, r))
        return dp[1][n]
