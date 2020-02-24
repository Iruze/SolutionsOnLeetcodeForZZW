- [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
> 给定一个由 **1**（陆地）和 **0**（水）组成的的二维网格，计算岛屿的数量。    
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。  

示例 1:
```shell
输入:
11110
11010
11000
00000

输出: 1
```     
示例 2:
```shell
输入:
11000
11000
00100
00011

输出: 3
```
运用**广度优先搜索BFS**和**深度优先搜索DFS**两种解法：
```python3
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
```

```python3                
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
```
