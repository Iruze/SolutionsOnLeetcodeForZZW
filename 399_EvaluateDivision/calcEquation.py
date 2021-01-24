"""
python3, 图+dfs 解法
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        var = set()
        for item, value in zip(equations, values):
            var.update(item)
            s, e = item[0], item[1]
            graph[s][e] = value
            graph[e][s] = 1.0 / value

        @functools.lru_cache(None)
        def dfs(s, e):
            if s == e:
                return 1.0
            visited.add(s)
            ret = 1.0
            for nxt in graph[s]:
                if nxt not in visited:
                    ret = graph[s][nxt] * dfs(nxt, e)
                    if ret > 0:
                        return ret
            visited.remove(s)
            return -1.0
        
        ans = list()
        visited = set()
        for s, e in queries:
            if s not in var or e not in var:
                ans.append(-1.0)
            else:
                visited.clear()
                ans.append(dfs(s, e))
        return ans
