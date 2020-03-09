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
