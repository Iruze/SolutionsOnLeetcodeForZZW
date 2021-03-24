class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area =0
        deque = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # 直接修改原数组， 访问过了就标记为-1
                    grid[r][c] = -1
                    deque.append((r, c))
                    max_area = max(max_area, self.__bfs(grid, deque))
        return max_area
    
    def __bfs(self, grid, deque):
        cur_area = 0
        while deque:
            r, c = deque.popleft()
            cur_area += 1
            for nr, nc in self.__neighbour(grid, r, c):
                deque.append((nr, nc))
        return cur_area

    def __neighbour(self, grid, r, c):
        rows, cols = len(grid), len(grid[0])
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                # 访问过了的(nr, nc)位置修改1为-1
                grid[nr][nc] = -1
                yield nr, nc
