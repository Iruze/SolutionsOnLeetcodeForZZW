class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen, curlen = 0, 0
        pos = dict()
        lo = 0
        # lo, hi 维护不重复的子串窗口
        for hi in range(len(s)):
            # 如果 s[hi] 在窗口，则更新左边lo
            if pos.get(s[hi], -1) >= lo:
                lo = pos[s[hi]] + 1
            curlen = hi - lo + 1
            pos[s[hi]] = hi
            maxlen = max(maxlen, curlen)
        return maxlen
