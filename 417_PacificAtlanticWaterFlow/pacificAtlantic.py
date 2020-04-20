class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix), len(matrix[0])
        def dfs(r, c, res):
            res.add((r, c))
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] <= matrix[nr][nc] and (nr, nc) not in res:
                    dfs(nr, nc, res)
        # 能够流入太平洋
        res1 = set()
        # 能够流入大西洋
        res2 = set()
        
        # 能够从北边流入太平洋的坐标
        for c in range(cols):
            dfs(0, c, res1)
        
        # 能够从西边流入太平洋
        for r in range(rows):
            dfs(r, 0, res1)
        
        # 从东边流入大西洋
        for r in range(rows):
            dfs(r, cols - 1, res2)
        
        # 从南边流入大西洋
        for c in range(cols):
            dfs(rows - 1, c, res2)
        
        return res1 & res2
