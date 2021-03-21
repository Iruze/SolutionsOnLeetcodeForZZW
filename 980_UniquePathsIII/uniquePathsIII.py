class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # rest表示能够访问的0和2的剩余的个数
        def dfs(r, c, rest):
            # 访问完所有的0和2了，且最后结束在2处
            if rest == 0 and grid[r][c] == 2:
                self.ans += 1
                return
            for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != -1:
                    visited[nr][nc] = True
                    dfs(nr, nc, rest - 1)
                    visited[nr][nc] = False
        
        # 定位起始方格，统计能够访问的0和2的个数rest
        rest, start = 0, None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or grid[r][c] == 2:
                    rest += 1
                if grid[r][c] == 1:
                    start = [r, c]
        
        self.ans = 0
        # 起始位置start标记为已访问
        visited[start[0]][start[1]] = True
        dfs(start[0], start[1], rest)
        return self.ans

    
# 方法二: 记忆化递归, 在上面解法基础之上, 存储已经走过的路径结果
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        pos = lambda r, c: 1 << (r * cols + c)

        rows, cols = len(grid), len(grid[0])
        travel_set = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] % 2 == 0:
                    travel_set |= pos(r, c)
                if grid[r][c] == 1:
                    sr, sc = r, c
        
        def neighbour(r, c):
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        @functools.lru_cache(None)
        def dfs(r, c, travel):
            if grid[r][c] == 2:
                return +(travel == 0)
            path_cnt = 0
            for nr, nc in neighbour(r, c):
                if pos(nr, nc) & travel:
                    path_cnt += dfs(nr, nc, pos(nr, nc) ^ travel)
            return path_cnt

        return dfs(sr, sc, travel_set)
        
