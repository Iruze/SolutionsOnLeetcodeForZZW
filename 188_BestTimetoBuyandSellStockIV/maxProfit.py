class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        # 如果 k > n // 2，按照k为无穷大处理
        if k > n // 2:
            return self.maxProfit_inf(prices)
        kmax = k
        dp = [[[0, 0] for _ in range(kmax + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(kmax, 0, -1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][kmax][0]

    
    # k为无穷大，此时状态方程忽略k的影响
    def maxProfit_inf(self, prices):
        d_i_0, d_i_1 = 0, -prices[0]
        for i in range(1, len(prices)):
            tmp = d_i_0
            d_i_0 = max(d_i_0, d_i_1 + prices[i])
            d_i_1 = max(d_i_1, tmp - prices[i])
        return d_i_0
