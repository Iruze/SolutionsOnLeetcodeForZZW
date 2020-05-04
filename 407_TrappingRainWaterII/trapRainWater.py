"""
1. 最外围作为围栏入最小堆；
2. 出堆，当前值是围栏的最矮的一个，搜索最矮的围栏周围
3. 内部柱子有比最矮围栏还矮的，则可以灌水；更新内部的这个柱子高度（选择原来高度和最矮围栏高度最大的那一个），
    并将这个柱子作为新的一格围栏和原来围栏组成新的外围栏，入堆
4. 重复 2，3：
"""

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        hp = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        # 最外围围栏入堆
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    # 最小堆，保证最矮的围栏出堆
                    heapq.heappush(hp, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        ans = 0
        while hp:
            h, r, c = heapq.heappop(hp)
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # 围栏比内部高，可以灌水
                    if h > heightMap[nr][nc]:
                        ans += h - heightMap[nr][nc]
                    # 忽略当前围栏，在(nr, nc)处新建围栏
                    visited[nr][nc] = True
                    # 新的围栏入堆
                    heapq.heappush(hp, (max(h, heightMap[nr][nc]), nr, nc))
        return ans
                    
