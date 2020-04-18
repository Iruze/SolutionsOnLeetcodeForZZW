class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[i][j] 代表(i, j)位置香槟的流量
        dp = [[0 for _ in range(query_row + 2)] for _ in range(query_row + 2)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j] += (dp[i][j] - 1) / 2
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2
        return min(1, dp[query_row][query_glass])
