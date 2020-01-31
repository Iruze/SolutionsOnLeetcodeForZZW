# 解法一： O(N2)空间效率
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])


# 解法二：O(N)空间效率
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        dp = [0] * len(triangle)
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            # 切记，dp[j]要依赖dp[j - 1]，先修改dp[j]，所以要倒着修改dp
            for j in range(i, -1, -1):
                if j == i:
                    dp[j] = dp[j - 1] + triangle[i][j]
                elif j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
        return min(dp)
                    
