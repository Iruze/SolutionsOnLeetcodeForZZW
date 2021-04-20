class Solution:
    def numSquares(self, n: int) -> int:
        """
        思想: 完全背包解法
        """
        square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
        
        dp = [n] * (n+1)
        # bottom case
        dp[0] = 0

        # 离散的选择在外循环
        for sq in square_nums:
            # 连续的选择在内循环, 且是正向的循环
            for i in range(sq, n + 1):
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[-1]
