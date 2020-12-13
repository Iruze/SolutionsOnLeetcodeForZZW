class Solution:

    def __init__(self):
        self.parent = dict()
        self.size = dict()
        self.count = 0

    def initialize(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = {i : 1 for i in range(n)}
        self.count = n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        # 路径压缩，size记录两颗树大小
        # 小的树接到大的树上，保持新树平衡
        if self.size[rootq] < self.size[rootp]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        # 两颗树连接后，树的总数减1
        self.count -= 1

    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        self.initialize(n)
        for i in range(n):
            # 只需要遍历对角线（不含对角线）右边的一半
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    self.union(i, j)
        return self.count
