class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        minLen = float('Inf')
        lo, hi = 0, 0
        window = Counter()
        t = Counter(t)
        while hi < len(s):
            # 入窗
            window[s[hi]] += 1
            # 维护窗口大小
            while all(map(lambda x: window[x] >= t[x], t.keys())):
                # 筛选符合条件的最短长度
                if hi - lo + 1 < minLen:
                    ans = s[lo:hi+1]
                    minLen = hi - lo + 1
                # 出窗
                window[s[lo]] -= 1
                lo += 1
            # 窗口右端右移
            hi += 1
        return ans
