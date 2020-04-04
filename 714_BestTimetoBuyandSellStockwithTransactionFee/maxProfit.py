class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        n = len(prices)
        d_i_0 = 0
        d_i_1 = -prices[0] - fee        # 第一天就买入
        for i in range(1, n):
            tmp = d_i_0
            d_i_0 = max(d_i_0, d_i_1 + prices[i])
            d_i_1 = max(d_i_1, tmp - prices[i] - fee)   # 当前天买入
        return d_i_0
