# python3 滑动窗口O(n)，每次取10个，如果当前的10个子串曾经访问过，则加入结果集:

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = set()
        ans = set()
        # 滑动窗口 [lo, hi] 大小维护为10
        lo, hi = 0, 9
        while hi < len(s):
            if s[lo:hi+1] in visited:
                ans.add(s[lo:hi+1])
            visited.add(s[lo:hi+1])
            lo, hi = lo + 1, hi + 1
        return list(ans)
