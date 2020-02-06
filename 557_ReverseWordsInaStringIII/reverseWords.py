class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([s1[::-1] for s1 in s.split(' ')])
