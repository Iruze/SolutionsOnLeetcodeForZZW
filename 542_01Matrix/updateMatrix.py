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
