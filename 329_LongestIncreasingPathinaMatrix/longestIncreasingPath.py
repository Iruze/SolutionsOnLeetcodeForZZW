class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(r, c):
            if lookup[r][c]:
                return lookup[r][c]
            res = 1
            # 向相邻的四个方向搜索
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] < matrix[nr][nc]:
                    res = max(res, 1 + dfs(nr, nc))
            lookup[r][c] = res
            return lookup[r][c]
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        lookup = [[0 for _ in range(cols)] for _ in range(rows)]
        return max(dfs(r, c) for r in range(rows) for c in range(cols))
