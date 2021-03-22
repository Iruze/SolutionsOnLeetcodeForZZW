# 方法一： 回溯+递归 （超时）
class Solution:
    def numOfWays(self, n):
        rows, cols = n, 3
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        self.ans = 0

        def backtrack(r, c):
            if r == rows:
                return True
            if c == cols:
                return backtrack(r + 1, 0)
            for i in range(1, 4):
                if not isvalid(r, c, i):
                    continue
                dp[r][c] = i
                if backtrack(r, c + 1):
                    self.ans += 1
            return False
        
        def isvalid(r, c, i):
            for nr, nc in ((r - 1, c), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and dp[nr][nc] == i:
                    return False
            return True

        backtrack(0, 0)
        return self.ans % (10 ** 9 + 7)




# 方法二： 数学规律
# 参考： https://leetcode-cn.com/problems/number-of-ways-to-paint-n-x-3-grid/solution/shu-xue-jie-jue-fei-chang-kuai-le-by-lindsaywong/
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        第一层： ABA(6),        ABC(6
        第二层： 3ABA+2ABC      2ABA+2ABC
        第三层： ......         ......
        """
        ABA, ABC = 6, 6
        MOD = 10 ** 9 + 7
        for i in range(2, n + 1):
            """
            当前 ABA : 下一层 BAB, BAC, BCB, CAB, CAC --> 3*ABA + 2*ABC
            当前 ABC : 下一层 BAB, BCA, BCB, CAB --> 2*ABA + 2*ABC
            """
            ABA, ABC = 3 * ABA + 2 * ABC, 2 * (ABC + ABA)
            ABA %= MOD
            ABC %= MOD
        return (ABC + ABA) % MOD
