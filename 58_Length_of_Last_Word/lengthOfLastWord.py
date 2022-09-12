class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(' ')[-1].strip()
        return len(s) if s else 0
