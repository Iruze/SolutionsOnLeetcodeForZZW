class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group = dict()
        # dfs判断是否可以将节点i放在组g中去，默认放在组1
        def dfs(i, g = 1):
            if i in group:
                return group[i] == g 
            group[i] = g
            # 将节点i相邻的所有节点放在组-1中，如果不存在任何冲突，则返回True
            return all(dfs(j, -1 * g) for j in graph[i])
        
        return all(dfs(i) for i in range(len(graph)) if i not in group)
