class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    # 如果以(i, j)开始的岛屿,是一条封闭的,结果+1
                    cnt += self._isLand(grid, i, j)
        return cnt
    
    def _isLand(self, grid, i, j):
        # 默认当前岛屿是"封闭的"
        bingo = True
        # 将当前岛屿位置置为2, 避免重复访问, 省下visited的 m*n 空间
        grid[i][j] = 2
        rows, cols = len(grid), len(grid[0])
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            # 在边界的1显然不是封闭的岛屿
            if not (0 <= ni < rows and 0 <= nj < cols):
                bingo = False
            # 邻接0,继续dfs递归搜索
            elif grid[ni][nj] == 0:
                # 利用 & "短路"性质
                bingo = self._isLand(grid, ni, nj) and bingo
        return bingo
