# 动态规划一： 二维
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0                            # 第一天没有买入，收益=0
        dp[0][1] = -prices[0]                   # 第一天买入，收益为-prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


# 动态规划二： 一维
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        d_i_0 = 0       # 第一天没有买入，收益=0
        d_i_1 = -prices[0]      # 第一天买入，收益为-prices[0]
        # 从第二天开始算
        for i in range(1, len(prices)):
            tmp = d_i_0     # 保存d_i_0，对于二维中是dp[i - 1][0]
            d_i_0 = max(d_i_0, d_i_1 + prices[i])
            d_i_1 = max(d_i_1, tmp - prices[i])
        return d_i_0
