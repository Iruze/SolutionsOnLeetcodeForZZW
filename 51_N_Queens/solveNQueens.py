import numpy as np


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cur = np.full((n, n), '.', dtype=str)
        def dfs(cur, r):
            if r == n:
                ans.append([''.join(p) for p in cur])
                return
            for c in range(n):
                if isvalid(cur, r, c):
                    cur[r][c] = 'Q'
                    dfs(cur, r + 1)
                    cur[r][c] = '.'
        def isvalid(cur, r, c):
            # 同一列
            if 'Q' in cur[:, c]: return False
            # 同一平行于主对角线
            if 'Q' in np.diag(cur, c - r): return False
            # 同一平行于辅对角线
            if 'Q' in np.diag(np.rot90(cur), r + c - n + 1): return False
            return True
        dfs(cur, 0)
        return ans
