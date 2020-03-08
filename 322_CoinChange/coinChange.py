class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 1: return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], 1 + dp[j - coin])
        return dp[amount] if dp[amount] <= amount else -1
