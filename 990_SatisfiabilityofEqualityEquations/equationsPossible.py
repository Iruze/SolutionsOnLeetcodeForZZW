class Solution:
    def __init__(self):
        self.count = 0
        self.size = []
        self.parent = []
    
    def initialize(self, totoal_node):
        self.count = totoal_node
        self.size = [1] * totoal_node
        self.parent = [i for i in range(totoal_node)]
    
    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        self.count -= 1
    
    def connected(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        return rootp == rootq
    
    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def equationsPossible(self, equations: List[str]) -> bool:
        # 26 个英文字母
        self.initialize(26)
        # 先让相等的字母形成连通分量
        for eq in equations:
            if eq[1] == '=':
                node1, node2 = eq[0], eq[3]
                self.union(ord(node1) - ord('a'), ord(node2) - ord('a'))
        # 检查不等关系是否打破相等关系的连通性
        for eq in equations:
            if eq[1] == '!':
                node1, node2 = eq[0], eq[3]
                # 如果相等关系成立，就是逻辑冲突
                if self.connected(ord(node1) - ord('a'), ord(node2) - ord('a')):
                    return False
        return True
