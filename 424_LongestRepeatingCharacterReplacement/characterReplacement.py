class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        maxstring = 0
        lo, hi = 0, 0
        ans = 0
        while hi < len(s):
            count[s[hi]] += 1
            maxstring = max(maxstring, count[s[hi]])
            if hi - lo + 1 - maxstring > k:
                count[s[lo]] -= 1
                lo += 1
            ans = max(ans, hi - lo + 1)
            hi += 1
        return ans
        
