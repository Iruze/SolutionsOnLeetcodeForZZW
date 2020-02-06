class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([s1.strip() for s1 in s.strip().split(' ') if s1][::-1])
