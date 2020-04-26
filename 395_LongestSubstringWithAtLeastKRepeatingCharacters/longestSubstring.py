# 分治-递归 思想

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        # 找到s中出现最少的字符
        t = min(set(s), key=s.count)
        # 最少出现的字符都大于等于K, s即最长子串
        if s.count(t) >= k:
            return len(s)
        # 分治思想，递归求得最长子串
        return max(self.longestSubstring(a, k) for a in s.split(t))
