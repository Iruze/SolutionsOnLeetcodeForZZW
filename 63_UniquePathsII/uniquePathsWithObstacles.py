class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] != 0 or obstacleGrid[m - 1][n - 1] != 0:
            return 0
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 0:
                    if i == 0:
                        dp[j:] = [0] * (n - j + 1)
                        break
                    else:
                        dp[j] = 0
                elif i == 0:
                    dp[j] = 1
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]
