class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()
        m = len(s)
        for i in range(m):
            if s[i] not in d1: d1[s[i]] = i
            if t[i] not in d2: d2[t[i]] = i
        for i in range(m):
            if d1[s[i]] != d2[t[i]]: return False
        return True
