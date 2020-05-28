class Solution:
    def balancedString(self, s):
        import collections
        count = collections.Counter(s)
        n = len(s)
        ans = n
        lo, hi = 0, 0
        while hi < n:
            count[s[hi]] -= 1
            while lo < n and count['Q'] <= n // 4 and count['W'] <= n // 4 and count['E'] <= n // 4 and count['R'] <= n // 4:
                ans = min(ans, hi - lo + 1)
                count[s[lo]] += 1
                lo += 1
            hi += 1
        return ans
