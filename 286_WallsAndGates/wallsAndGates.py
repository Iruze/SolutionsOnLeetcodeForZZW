class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return rooms
        INF = 2147483647
        queue = collections.deque()
        rows, cols = len(rooms), len(rooms[0])
        for r, row in enumerate(rooms):
            for c, val in enumerate(row):
                if val == 0: queue.append((r, c))
        
        def neibours(r, c):
            for nr, nc in ((r, c + 1), (r , c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc
        
        while queue:
            r, c = queue.popleft()
            for nr, nc in neibours(r, c):
                if rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
        
        return rooms
