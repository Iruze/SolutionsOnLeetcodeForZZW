import collections


class UF():
    def __init__(self):
        self.parent = {}
    
    def find(self, x):
        # 做了路径压缩
        self.parent.setdefault(x, x)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, p, q):
        self.parent[self.find(q)] = self.find(p)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF()
        email_to_name = dict()
        ans = collections.defaultdict(list)
        for account in accounts:
            for i in range(1, len(account)):
                # email - name 一对一映射
                email_to_name[account[i]] = account[0]
                # 1. 连接
                if i < len(account) - 1:
                    uf.union(account[i], account[i + 1])
        # 2. 合并
        for email in email_to_name:
            ans[uf.find(email)].append(email)
        return [[email_to_name[value[0]]] + sorted(value) for value in ans.values()]
