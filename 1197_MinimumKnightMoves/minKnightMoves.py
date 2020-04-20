class Solution:
    def minKnightMoves(self, x, y):
        if x == 0 and y == 0:
            return 0
        # 只关注第一象限
        x, y = abs(x), abs(y)
        visited = set()
        cur, nxt = [], []
        cur.append((0, 0))
        steps = 1
        while cur:
            for r, c in cur:
                for nr, nc in self.neighbour(r, c):
                    # 向(x, y)点附近扩散
                    if -2 < nr < x + 3 and -2 < nc < y + 3 and (nr, nc) not in visited:
                        if nr == x and nc == y:
                            return steps
                        visited.add((nr, nc))
                        nxt.append((nr, nc))
            cur, nxt = nxt, []
            steps += 1
        return -1
    
    def neighbour(self, r, c):
        offset = [-2, -1, 1, 2]
        return [(r + i, c + j) for i in offset for j in offset if abs(i) != abs(j)]
