# BFS模板
BFS的模板有两种，
```shell
1. 所有的源先入队——>统一bfs；
2. 先单点源入队——>单点源bfs，所有的源过一遍
```

#### BFS模板一
```python3
# 单源入队
def mainFun():
  ...
  for r in range(rows): 
    for c in range(cols):
      if matrix[r][c] == 0 and not visited[r][c]:
        self._bfs(matrix, r, c, visited)
...

def _bfs(self, matrix, r, c, visited):
  d = deque()
  d.append((r, c))
  while d:
    r, c = d.popleft()
    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
      ...
```

#### BFS模板二
```python3
# 多源入队
def mainFun():
  ...
  for r in range(rows):
    for c in range(cols):
      if matrix[r][c] == 0:
        d.append((r, c))
        ...
while d:
  r, c = d.popleft()
  for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
    ...
```

**单源和多源的区别：**
<details>
<summary>展开</summary>
  
- 单源按个遍历源，每个源调用一次bfs()        
  多源先所有源入队，紧接着直接 **出队-入队** 广度搜索；

- 单源有单独的bfs函数     
  多源bfs写在当前函数内
  
</details>


# 例题

**【模板一】**
- [994. 腐烂的橘子](https://leetcode-cn.com/problems/rotting-oranges/)
> 在给定的网格中，每个单元格可以有以下三个值之一：      
值 0 代表空单元格；     
值 1 代表新鲜橘子；   
值 2 代表腐烂的橘子。      
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。       
返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。    

```shell
示例 1:

输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
```

解法：
```python3
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        rows, cols = len(grid), len(grid[0])
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neibours(r, c):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neibours(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))
        
        if any(1 in row for row in grid):
            return -1
        return d
```

**【模板二】**
- [542. 01 矩阵](https://leetcode-cn.com/problems/01-matrix/)
> 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。   
两个相邻元素间的距离为 1 。
```shell
示例 2:
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
```
解法：
```python3
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        d = collections.deque()
        for r in range(rows):
            for c in range(cols):
                # 首先将所有的 0 都入队，并且将 1 的位置设置成 -1，表示该位置是 未被访问过的 1
                if matrix[r][c] == 0:
                    d.append((r, c))
                else:
                    matrix[r][c] = -1
        
        while d:
            r, c = d.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                # 如果四邻域的点是 -1，表示这个点是未被访问过的 1
                # 所以这个点到 0 的距离就可以更新成 matrix[x][y] + 1。
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == -1:
                    matrix[nr][nc] = matrix[r][c] + 1
                    d.append((nr, nc))
        return matrix
```
其他：   
-[1162. 地图分析](https://leetcode-cn.com/problems/as-far-from-land-as-possible/)
