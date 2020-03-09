# 解法一：双指针解法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isValid(s):
            return '0' <= s <= '9' or 'a' <= s <= 'z' or 'A' <= s <= 'Z'
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


# 解法二： 运用filter函数
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [*filter(str.isalnum, s.lower())]
        return s == s[::-1]
