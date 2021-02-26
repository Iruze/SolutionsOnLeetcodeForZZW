class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @functools.lru_cache(None)
        def match(i, j):
            if j == len(p): return i == len(s)
            # cur记录当前单个字符: s[i]和p[j]匹配的情况
            cur = (i < len(s) and p[j] in {s[i], '.'})
            if j < len(p) - 1 and p[j + 1] == '*':
                return match(i, j + 2) or cur and match(i + 1, j)
            return cur and match(i + 1, j + 1)
        
        return match(0, 0)
 
