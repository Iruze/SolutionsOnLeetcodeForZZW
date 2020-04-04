class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0, 0] for i in range(n)]
        for i in range(n):
            # 因为冷冻期，base case 分需单独考虑头两天的交易情况
            if i == 0:                  # 第一天的 base case
                dp[i][0] = 0
                dp[i][1] = -prices[0]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i == 1:                  # 第二天的 base case
                dp[i][1] = max(dp[0][1], -prices[i])
                continue
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0]
