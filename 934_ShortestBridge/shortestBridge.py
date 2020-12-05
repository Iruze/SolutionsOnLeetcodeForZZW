"""
染色法, 一次DFS + 一次BFS
1). "染色法"先将小岛1的所有位置标记为2, 并送入队列;
2). 所有队列中的所有位置, 向周围"扩散", 即继续"染色"
3). 当触及到小岛2(A[nr][nc] == 1), 立即返回结果
"""

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])
        island1 = collections.deque()
        collected = False
        # 将小岛1的所有位置加入到队列island1中
        for r in range(rows):
            if any(A[r]):
                c = A[r].index(1)
                # dfs深度遍历搜索所有小岛1的位置
                self._dfs(r, c, A, island1)
                break
        while island1:
            r, c = island1.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    # 触及到了小岛2, 返回结果
                    if A[nr][nc] == 1:
                        return A[r][c] - 2
                    # 只触及到了岛之间的水,继续'染色'
                    elif A[nr][nc] == 0:
                        A[nr][nc] = A[r][c] + 1
                        island1.append((nr, nc))
        return A[r][c] - 2
    
    def _dfs(self, r, c, A, island1):
        # 染色法: 将本来的'1'染成'2', 省去了传统的visited空间
        A[r][c] += 1
        island1.append((r, c))
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < len(A) and 0 <= nc < len(A[0]) and A[nr][nc] == 1:
                self._dfs(nr, nc, A, island1)
