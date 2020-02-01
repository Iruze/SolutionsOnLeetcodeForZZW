# 解法一： 贪心算法
# 参考：https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return pow(3, a)
        if b == 1: return pow(3, a - 1) * 4
        return pow(3, a) * b
        
# 解法二： 动态规划一：
# 传统的dp
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
        return dp[n]
    
# 解法三：动态规划二：
# j只关心2和3，大于3的必然化为2和3
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        dp[0] = 0
        for i in range(3, n + 1):
            dp[i] = max(max(dp[i - 1], i - 1), 
            2 * max(dp[i - 2], i - 2), 
            3 * max(dp[i - 3], i - 3))
        return dp[n]
