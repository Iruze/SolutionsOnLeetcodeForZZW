# 方法一：dfs + 备忘录
class Solution:
    def __init__(self):
        self.d = dict()
    

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def onceProbability(r, c):                                   # 搜索能够到达的棋盘上的位置
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
        if K == 0:                                                    # DFS 的 base case
            return 1
        ans = 0
        for nr, nc in onceProbability(r, c):
            if (nr, nc, K) in self.d:
                nxt_prob = self.d[(nr, nc, K)]                         # 如果备忘录中存在(nr, nc, K), 
            else:                   
                nxt_prob = self.knightProbability(N, K - 1, nr, nc)    # DFS返回下一个概率
                self.d[(nr, nc, K)] = nxt_prob                         # 如果备忘录中不存在，则加入
            ans += 0.125 * cur
        return ans
