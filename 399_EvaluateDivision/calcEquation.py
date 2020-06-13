"""
python3, 图+dfs 解法
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(dict)
        var = set()
        ans = []
        for item, value in zip(equations, values):
            var.update(item)
            s, e = item[0], item[1]
            graph[s][e] = value
            graph[e][s] = 1.0 / value
        
        def dfs(s, e, visited):
            if s == e:
                return 1.0
            visited.add(s)
            rnt = 1.0
            for nxt in graph[s]:
                if nxt not in visited:
                    rnt = graph[s][nxt] * dfs(nxt, e, visited)
                    if rnt > 0:
                        return rnt
            return -1
        
        for s, e in queries:
            if s not in var or e not in var:
                ans.append(-1.0)
            else:
                ans.append(dfs(s, e, set()))
        
        return ans
