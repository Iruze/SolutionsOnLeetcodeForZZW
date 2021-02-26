class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        minLen = float('Inf')
        lo, hi = 0, 0
        window = Counter()
        t = Counter(t)
        cnt = 0                 # 记录窗口中的字符串中包含t中字符的个数
        while hi < len(s):
            # 入窗
            window[s[hi]] += 1
            cnt += (window[s[hi]] == t[s[hi]])
            # 当窗口包含了全部的t的字符
            while cnt == len(t):
                # 筛选符合条件的最短长度
                if hi - lo + 1 < minLen:
                    ans = s[lo:hi+1]
                    minLen = hi - lo + 1
                # 出窗
                window[s[lo]] -= 1
                # 当左端出窗的字符在t中,且小于t中的个数
                cnt -= (window[s[lo]] < t[s[lo]])
                lo += 1
            # 窗口右端右移
            hi += 1
        return ans
