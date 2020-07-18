class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # 将dislike画成联通的无向图
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = dict()
        def dfs(i, c = 1):
            if i in color:
                return c == color[i]
            # 节点i未染色，和i相邻的节点也未染色，故默认染色为1
            color[i] = c
            # 将节点i的所有相邻节点染色为-1，都不存在染色冲突则返回True
            return all(dfs(j, -1 * c) for j in graph[i])
        
        return all(dfs(i) for i in range(1, N + 1) if i not in color)
