from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        count_odd = [x for x in c.values() if x % 2 != 0]
        return len(s) - len(count_odd) + 1 if count_odd else len(s)
