class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        # 边界不用搜索
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if not visited[r][c] and board[r][c] == 'O':
                    self._bfs(board, r, c, visited)
    
    def _bfs(self, board, r, c, visited):
        visited[r][c] = True
        rows, cols = len(board), len(board[0])
        d, store = collections.deque(), []
        d.append((r, c))
        surround =  True
        while d:
            r, c = d.popleft()
            # store用来暂存当前的‘O’位置, 万一它是可包围的就要置为'X'了
            store.append((r, c))
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O' and not visited[nr][nc]:
                    # 标记所有已访问过的元素，达到剪枝的目的
                    visited[nr][nc] = True
                    # 触到边界，一定是不可包围的
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        surround = False
                    else:
                        d.append((nr, nc))
        # 是可包围的，则直接置store中所有的'O'为'X'
        if surround:
            for r, c in store:
                board[r][c] = 'X'
        return
