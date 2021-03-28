class Solution:

    @lru_cache(None)
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def onceProbability(r, c):
            board = [
                (r + 2, c + 1),
                (r + 2, c - 1),
                (r - 2, c + 1),
                (r - 2, c - 1), 
                (r + 1, c + 2), 
                (r + 1, c - 2), 
                (r - 1, c + 2), 
                (r - 1, c - 2)
            ]
            for nr, nc in board:
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc
        
        if K == 0: return 1
        f = self.knightProbability
        nbr = onceProbability(r, c)
        # 如果不能跳到相邻的格子, 概率返回0
        return sum(0.125 * f(N, K - 1, nr, nc) for nr, nc in nbr) if nbr else 0
