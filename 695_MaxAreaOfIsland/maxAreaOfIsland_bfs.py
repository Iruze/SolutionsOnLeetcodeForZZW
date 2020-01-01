class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        deque = collections.deque()
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    visited[r][c] = True
                    deque.append((r, c))
                    cur_area = self.__bfs(rows, cols, grid, visited, deque)
                    max_area = max(max_area, cur_area)
        return max_area
    
    def __bfs(self, rows, cols, grid, visited, deque):
        cur_area = 0
        while deque:
            r, c = deque.popleft()
            cur_area += 1
            for nr, nc in self.__neighbour(r, c, grid, visited):
                visited[nr][nc] = True
                deque.append((nr, nc))
        return cur_area

    def __neighbour(self, r, c, grid, visited):
        rows, cols = len(grid), len(grid[0])
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and not visited[nr][nc]:
                yield nr, nc
