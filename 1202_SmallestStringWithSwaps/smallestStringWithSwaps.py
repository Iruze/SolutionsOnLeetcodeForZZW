class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {i: i for i in range(len(s))}

        # 找到根节点root
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        # def connect(p, q), 连接节点p, q
        for p, q in pairs:
            parent[find(p)] = find(q)
        # 对每一个联通的集合排序
        d = collections.defaultdict(list)
        for i, v in enumerate(map(find, parent)):
            d[v].append(i)
        # 按照字典序，插入到结果ans中去
        ans = list(s)
        for seq in d.values():
            words = sorted(ans[i] for i in seq)
            for i, c in zip(sorted(seq), words):
                ans[i] = c
        return ''.join(ans)

    
    
    
    
    
# 并查集的完整解法
class Solution:
    
    def __init__(self):
        self.parent = dict()
        self.size = dict()

    def initialize(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        else:
            self.parent[rootp] = rootq
            self.size[rootq] += self.size[rootp]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.initialize(n)
        for p, q in pairs:
            self.union(p, q)
        d = collections.defaultdict(list)
        for i, val in enumerate(map(self.find, self.parent)):
            d[val].append(i)
        ans = ['' for _ in range(n)]
        for seq in d.values():
            words = sorted(s[idx] for idx in seq)
            for i, c in zip(seq, words):
                ans[i] = c
        return ''.join(ans)
