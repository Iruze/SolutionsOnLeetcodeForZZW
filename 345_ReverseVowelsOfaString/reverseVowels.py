class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while s[lo].lower() not in vowels and lo < hi:
                lo += 1
            while s[hi].lower() not in vowels and lo < hi:
                hi -= 1
            if lo < hi:
                s[lo], s[hi] = s[hi], s[lo]
                lo, hi = lo + 1, hi - 1
        return ''.join(s)
