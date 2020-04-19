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
