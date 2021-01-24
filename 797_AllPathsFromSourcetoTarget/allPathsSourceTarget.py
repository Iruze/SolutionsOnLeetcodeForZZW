class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        @functools.lru_cache(None)              # 缓存dfs中间结果，降低复杂度
        def dfs(i):
            if i == n - 1:                      # base case
                return [[n - 1]]
            tmp = []
            for nbr in graph[i]:
                for path in dfs(nbr):
                    tmp.append([i] + path)      # i点出发的路径合成
            return tmp
        
        return dfs(0)
