# 方法一： dfs
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    ans += self._dfs(r, c, grid)
        return ans

    def _dfs(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] == 1:
            return 1
        grid[r][c] = 1
        ret = 1
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            ret = min(ret, self._dfs(nr, nc, grid))
        return ret
        
# 方法二： bfs
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    ans += self._bfs(r, c, grid)
        return ans

    def _bfs(self, r, c, grid):
        d = collections.deque()
        d.append((r, c))
        ret = 1
        rows, cols = len(grid), len(grid[0])
        while d:
            r, c = d.popleft()
            grid[r][c] = 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    ret = 0
                    continue
                if grid[nr][nc] == 0:
                    d.append((nr, nc))
        return ret
