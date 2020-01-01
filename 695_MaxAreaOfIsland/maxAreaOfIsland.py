# 解法一： 深度优先搜索dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    cur_area = self.__dfs(r, c, rows, cols, grid, visited)
                    max_area = max(max_area, cur_area)
        return max_area
    
    def __dfs(self, r, c, rows, cols, grid, visited):
        cur_area = 1
        visited[r][c] = True
        for nr, nc in self.__neighbour(r, c, rows, cols, grid, visited):
            cur_area += self.__dfs(nr, nc, rows, cols, grid, visited)
        return cur_area

    def __neighbour(self, r, c, rows, cols, grid, visited):
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                yield nr, nc
