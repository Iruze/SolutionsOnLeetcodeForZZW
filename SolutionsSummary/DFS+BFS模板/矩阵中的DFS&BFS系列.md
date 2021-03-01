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
<details>
    <summary>解法一： 深度优先搜索dfs</summary>
    
```python3
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
</details>


<details>
    <summary>解法二： 广度优先搜索bfs</summary>
    
```python3                
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
</details>


# **染色法**代替了传统的标记访问`visited`
- [934. 最短的桥](https://leetcode-cn.com/problems/shortest-bridge/)
> 在给定的二维二进制数组 `A` 中，存在两座岛。（岛是由四面相连的 `1` 形成的一个最大组。）          
现在，我们可以将 `0` 变为 `1`，以使两座岛连接起来，变成一座岛。            
返回必须翻转的 `0` 的最小数目。（可以保证答案至少是 `1`。）      

示例 1：
```
输入：[[0,1],[1,0]]
输出：1
```

染色法, 一次DFS + 一次BFS
>1). "染色法"先将小岛1的所有位置标记为2, 并送入队列;        
2). 所有队列中的所有位置, 向周围"扩散", 即继续"染色"            
3). 当触及到小岛2(A[nr][nc] == 1), 立即返回结果     

<details>
    <summary>解法</summary>
    
```python
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        island1 = collections.deque()
        collected = False
        # 将小岛1的所有位置加入到队列island1中
        for r in range(rows):
            if any(A[r]):
                c = A[r].index(1)
                # dfs深度遍历搜索所有小岛1的位置
                self._dfs(r, c, A, island1)
                break
        while island1:
            r, c = island1.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    # 触及到了小岛2, 返回结果
                    if A[nr][nc] == 1:
                        return A[r][c] - 2
                    # 只触及到了岛之间的水,继续'染色'
                    elif A[nr][nc] == 0:
                        A[nr][nc] = A[r][c] + 1
                        island1.append((nr, nc))
        return A[r][c] - 2
    
    def _dfs(self, r, c, A, island1):
        # 染色法: 将本来的'1'染成'2', 省去了传统的visited空间
        A[r][c] += 1
        island1.append((r, c))
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < len(A) and 0 <= nc < len(A[0]) and A[nr][nc] == 1:
                self._dfs(nr, nc, A, island1)
```
</details>

[286. 墙与门](https://leetcode-cn.com/problems/walls-and-gates/)
> 你被给定一个 `m × n` 的二维网格，网格中有以下三种可能的初始化值：         
`-1` 表示墙或是障碍物           
`0` 表示一扇门           
`INF` 无限表示一个空的房间。然后，我们用 `231 - 1 = 2147483647` 代表 `INF`。你可以认为通往门的距离总是小于 `2147483647` 的。         
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。         

示例：
```shell
给定二维网格：

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```

<details>
    <summary>解法</summary>
    
```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return rooms
        INF = 2147483647
        queue = collections.deque()
        rows, cols = len(rooms), len(rooms[0])
        # 第一步: 收集门 0
        for r, row in enumerate(rooms):
            for c, val in enumerate(row):
                if val == 0: queue.append((r, c))
        
        def neibours(r, c):
            for nr, nc in ((r, c + 1), (r , c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc
        
        while queue:
            # 围绕"门"进行染色
            r, c = queue.popleft()
            for nr, nc in neibours(r, c):
                if rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
        
        return rooms
```
</details>
