"""
dfs + bfs解法：
dfs将第一个岛的1全部入队，bfs扩散搜索入队的第一个岛的1到第二个岛的1的距离。
"""
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        d = collections.deque()
        collected = False
        for r in range(rows):                   # dfs搜索，将第一个岛中1全部入队
            if any(A[r]):
                c = A[r].index(1)
                self._dfs(r, c, A, d)
                break
        
        while d:                                # bfs扩散，找到到达1的距离
            r, c = d.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    if A[nr][nc] == 1:          # 找到了，它就是第二个岛
                        return A[r][c] - 2      # 第一个岛本身值为1， 为了标记已经访问，加了1以区分，所以结果要减去2
                    elif A[nr][nc] == 0:
                        A[nr][nc] = A[r][c] + 1
                        d.append((nr, nc))
        return A[r][c] - 2
    
    def _dfs(self, r, c, A, d):
        A[r][c] += 1
        d.append((r, c))
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < len(A) and 0 <= nc < len(A[0]) and A[nr][nc] == 1:
                self._dfs(nr, nc, A, d)
