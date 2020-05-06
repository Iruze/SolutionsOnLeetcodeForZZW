import numpy as np


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(r, cur):
            # 递归完所有的n行，说明是有效的皇后摆放
            if r == n:
                self.ans += 1
                return
            for c in range(n):
                # 回溯求得皇后的摆放
                if isvalid(r, c, cur):
                    cur[r][c] = 'Q'
                    backtrack(r + 1, cur)
                    cur[r][c] = '.'
        def isvalid(r, c, cur):
            # 在同一列否
            if 'Q' in cur[:, c]: return False
            # 在同一主对角线否
            if 'Q' in np.diag(cur, c - r): return False
            # 在同一辅对角线否
            if 'Q' in np.diag(np.rot90(cur), r + c - n + 1): return False
            return True

        cur = np.full((n, n), '.', dtype=str)
        self.ans = 0
        backtrack(0, cur)
        return self.ans
