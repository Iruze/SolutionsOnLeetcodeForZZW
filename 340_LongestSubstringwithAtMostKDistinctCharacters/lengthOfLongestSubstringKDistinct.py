class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        lo, hi = 0, 0
        window = collections.defaultdict(int)
        # 窗口内的不同字符串个数
        cnt = 0
        while hi < len(s):
            # 啥也别管，先入窗就完事了
            window[s[hi]] += 1
            # window[s[hi]] == 1，说明s[hi]是新来的，cnt加1
            cnt += 1 if window[s[hi]] == 1 else 0
            # 维护窗口大小为k，其实也可以不用cnt，写成 while len(window.keys()) > k
            # 对应地，在window[s[lo]] = 0时候需要删掉s[lo]： del window[s[lo]]
            while cnt > k:
                window[s[lo]] -= 1
                # window[s[lo]] == 0 说明要收缩的左端lo的字符在窗口内唯一
                cnt -= 1 if window[s[lo]] == 0 else 0
                lo += 1
            ans = max(ans, hi - lo + 1)
            hi += 1
        return ans
