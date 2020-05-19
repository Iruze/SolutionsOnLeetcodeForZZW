class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        N = len(graph)

        def dfs(node):
            if node == N - 1:
                return [[N - 1]]
            
            ans = []
            for nei in graph[node]:
                for path in dfs(nei):
                    ans.append([node] + path)
            return ans

        return dfs(0)
