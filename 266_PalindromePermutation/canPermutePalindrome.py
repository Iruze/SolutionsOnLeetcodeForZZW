from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s: return True
        c = Counter(s)
        even = [x for x in c.values() if x % 2 == 0]
        odd = [x for x in c.values() if x % 2 != 0]
        return len(odd) < 2
