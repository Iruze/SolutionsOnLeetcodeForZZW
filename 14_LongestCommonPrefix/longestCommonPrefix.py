class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        s_min, s_max = min(strs), max(strs)
        for i, c in enumerate(s_min):
            if c != s_max[i]:
                return s_min[:i]
        return s_min
