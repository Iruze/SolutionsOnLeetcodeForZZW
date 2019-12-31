# 解法一： 深度优先搜索dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        visted = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visted[i][j]:
                    count += 1
                    self.__dfs(grid, i, j, m, n, visted)
        return count
    
    def __dfs(self, grid, i, j, m, n, visted):
        visted[i][j] = True
        for nr, nc in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= nr < m and 0 <= nc < n and not visted[nr][nc] and grid[nr][nc] == '1':
                self.__dfs(grid, nr, nc, m, n, visted)

                
# 解法二： 广度优先搜索bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        visted = [[False for _ in range(n)] for _ in range(m)]
        deque = collections.deque()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visted[i][j]:
                    count += 1
                    self.__bfs(grid, i, j, m, n, visted, deque)
        return count
    
    def __bfs(self, grid, i, j, m, n, visted, deque):
        visted[i][j] = True
        deque.append((i, j))
        while deque:
            ci, cj = deque.popleft()
            for nr, nc in self.__neighbour(ci, cj, m, n, grid, visted):
                deque.append((nr, nc))
                visted[nr][nc] = True
    
    def __neighbour(self, i, j, m, n, grid, visted):
        for nr, nc in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and not visted[nr][nc]:
                yield nr, nc
