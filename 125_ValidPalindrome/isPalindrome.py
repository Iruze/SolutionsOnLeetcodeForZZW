class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isValid(s):
            return '0' <= s and s <= '9' or 'a' <= s and s <= 'z' or 'A' <= s and s <= 'Z'
        left, right = 0, len(s) - 1
        while left < right:
            if not isValid(s[left]):
                left += 1
                continue
            if not isValid(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
