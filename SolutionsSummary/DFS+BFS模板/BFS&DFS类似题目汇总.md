# 房间到门的距离 -> 门到房间的距离

> 这类题目: 将"房间->门"转换为"门->房间", 以"门"为起始点, 运动BFS向周围扩散

- [286. 墙与门](https://leetcode-cn.com/problems/walls-and-gates/)
> 你被给定一个 m × n 的二维网格 rooms ，网格中有以下三种可能的初始化值：
> 
```
-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近门的距离 ，如果无法到达门，则填 INF 即可。
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
        for r, row in enumerate(rooms):
            for c, val in enumerate(row):
                # 把所有的门入列
                if val == 0: queue.append((r, c))
        
        def neibours(r, c):
            for nr, nc in ((r, c + 1), (r , c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc
        
        while queue:
            r, c = queue.popleft()
            for nr, nc in neibours(r, c):
                # 从门向周围bfs扩散搜索
                if rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))

```
</details>

将 "海洋->陆地" 转化成了 "陆地->海洋", 以陆地为中心, 运用bfs向周围扩散
- [1162. 地图分析](https://leetcode-cn.com/problems/as-far-from-land-as-possible/)
> 你现在手里有一份大小为 N x N 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，     
请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的。        
我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 - x1| + |y0 - y1| 。        
如果网格上只有陆地或者海洋，请返回 -1。



<details>
    <summary>解法</summary>
    
```python
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        rows, cols = len(grid), len(grid[0])
        d = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    d.append((r, c))
        ans = -1
        while d:
            r, c = d.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    ans = max(ans, grid[nr][nc])
                    d.append((nr, nc))
        return ans - 1 if ans > 0 else -1
```
</details>
