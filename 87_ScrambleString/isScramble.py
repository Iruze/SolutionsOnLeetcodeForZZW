class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @functools.lru_cache(None)
        def dfs(s1, s2):
            if s1 == s2: return True
            if Counter(s1) != Counter(s2): return False
            for i in range(1, len(s1)):
                syn = dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:])
                mir = dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i])
                if syn or mir:
                    return True
            return False
        
        return dfs(s1, s2)
