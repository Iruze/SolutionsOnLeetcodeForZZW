class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        def backtrack(r, col, u_diag, d_diag):
            if r == n:
                return True
            for c in range(n):
                """
                当前皇后有效的条件，不在这三种线上（按行扫描排列'Q', 故必然不在同一行）：
                1). 同一列
                2). 主对角线，坐标之和相等
                3). 副对角线，坐标之差相等
                """
                if c not in col and r + c not in u_diag and r - c not in d_diag:
                    if backtrack(r + 1, {c} | col, {r + c} | u_diag, {r - c} | d_diag):
                        self.ans += 1
            return False
        backtrack(0, set(), set(), set())
        return self.ans
