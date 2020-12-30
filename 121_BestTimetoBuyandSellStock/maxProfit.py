# 解法一： 普通解法，
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return -0
        # min_v记录截止到目前的最低的股票价格
        min_v = prices[0]
        ans = 0
        for i, p in enumerate(prices):
            # 更新min_v
            min_v = min(min_v, p)
            ans = max(ans, p - min_v)
        return ans

# 解法二： dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        d_i_0 = 0
        d_i_1 = -prices[0]                              # 第一天买入，收益为 -prices[0]
        for i in range(1, len(prices)):                 # 注意: 是从第2天开始计算
            d_i_0 = max(d_i_0, d_i_1 + prices[i])       # 因为只有一次买入，所以当前买入，则收益为-prices[i]
            d_i_1 = max(d_i_1, -prices[i])              # 不同于多次买入，需要 d_i_0 - prices[i]
        return d_i_0
