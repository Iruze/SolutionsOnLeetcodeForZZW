class Solution:
    # 两两石头相碰，最终转化为求 A - B 的最小值
    # SUM = A + B， 则需要 B 接近 SUM/2， 从而转化为0-1背包问题
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        dp = [0 for _ in range(target + 1)]
        # 物件的选择在外循环
        for stone in stones:
            # 背包的重量是连续的，在内循环
            # 0-1背包采用逆序遍历，完全背包则是正序
            for i in range(target, stone - 1, -1):
                dp[i] = max(dp[i], dp[i - stone] + stone)
        return sum(stones) - 2 * dp[-1]
