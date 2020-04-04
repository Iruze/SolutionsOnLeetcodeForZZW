class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        # base case
        dp[0][0][0] = dp[0][1][0] = dp[0][2][0] = 0
        dp[0][1][1] = dp[0][2][1] = -prices[0]      # dp[0][0][1] 用不上，所以也不用管
        for i in range(1, n):
            for k in range(2, 0, -1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][2][0]
