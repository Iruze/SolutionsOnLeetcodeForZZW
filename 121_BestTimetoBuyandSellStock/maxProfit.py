# 解法一： 单调栈
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        diff = float('-Inf')
        for i in range(len(prices)):
            # stack维护一个单调递减的栈
            if not stack or prices[stack[-1]] > prices[i]:
                stack.append(i)
            # 更新diff
            elif prices[i] - prices[stack[-1]] > diff:
                    diff = prices[i] - prices[stack[-1]]
        return diff if diff > 0 else 0

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
