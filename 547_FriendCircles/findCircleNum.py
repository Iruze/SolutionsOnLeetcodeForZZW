class Solution:
    def __init__(self):
        self.tree_num = 0
        self.tree_node = []
        self.parent = []
    
    def initialize_tree(self, n):
        self.tree_num = n 
        self.tree_node = [1] * n 
        self.parent = [i for i in range(n)]

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.tree_node[p] > self.tree_node[q]:
            self.parent[rootp] = rootp
            self.tree_node[rootp] += self.tree_node[rootq]
        else:
            self.parent[rootp] = rootq
            self.tree_node[rootq] += self.tree_node[rootp]
        self.tree_num -= 1
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.initialize_tree(len(M))
        for i in range(len(M)):
            for j in range(i):
                if M[i][j] == 1:
                    self.union(i, j)
        return self.tree_num
