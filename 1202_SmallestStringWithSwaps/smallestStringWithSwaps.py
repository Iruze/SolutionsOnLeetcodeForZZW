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
