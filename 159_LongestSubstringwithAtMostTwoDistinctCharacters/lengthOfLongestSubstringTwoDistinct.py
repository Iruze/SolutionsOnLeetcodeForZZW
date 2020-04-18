"""
滑动窗口，window维护一个不同字符最多2个的窗口，大于2时， 出窗：
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        ans = 0
        lo, hi = 0, 0
        window = collections.deque()
        while hi < n:
            window.append(s[hi])
            # 维护不同字符数量的窗口，大小为2
            while len(set(window)) > 2:
                window.popleft()
                lo += 1
            ans = max(ans, hi - lo + 1)
            hi += 1
        return ans
