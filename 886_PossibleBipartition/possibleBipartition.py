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

    
    
# 缓存dfs搜索结果, 降低时间复杂度, O(n)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group = dict()

        @functools.lru_cache(None)              # 缓存dfs(i)的结果, 下一次相同的i相当于表查询, O(n)复杂度
        def dfs(i, g=1):
            if i in group:
                return group[i] == g            # group[i]和g是否矛盾
            group[i] = g
            for con in graph[i]:                # 如果i的所有邻接点都不矛盾,返回true
                if not dfs(con, -1 * g):
                    return False
            return True
        
        for i in range(len(graph)):             # 检查所有的0-(n-1), 如果都不矛盾,证明能够按照要求"安排"
            if i not in group and not dfs(i):   # 此处必须强调i不在group, 因为前面搜索中可能将
                return False                    # i判定给了-1, 但是此时如果再次dfs搜索, 将其默认为1,会矛盾
        return True
