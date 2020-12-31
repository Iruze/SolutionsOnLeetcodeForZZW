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

# 类似解法一： 染色法， 
"""
将所有遍历到的'1'都染色成'-1',标记成了"已访问"状态
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: 
            return 0
        rows, cols = len(grid), len(grid[0])
        
        # 将'1'的地方"染色",成为'-1',并dfs下去
        def color(r, c):
            grid[r][c] = '-1'
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    color(nr, nc)

        island = 0
        for r in range(rows):
            for c in range(cols):
                # 因为所有连起来的岛都已经被"染色"了,
                # 所以剩下的为'1'的地方必然是一个新的岛
                if grid[r][c] == '1':
                    island += 1
                    # 对新岛进行"染色"
                    color(r, c)
        return island

                
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
