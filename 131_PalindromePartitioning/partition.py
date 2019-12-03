class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        if s:
            self.__dfs(s, res, [])
        return res
    

    def __dfs(self, s, res, pre=[]):
        if s == s[::-1]:
            res.append(pre[:] + [s])
            if len(s) <= 1: return
        for i in range(1, len(s)):
            d, s = s[:i], s[i:]
            if d == d[::-1]:
                pre.append(d)
                self.__dfs(s, res, pre)
                pre.pop()
            s = d + s
