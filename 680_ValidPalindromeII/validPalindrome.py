""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                  solution1:   递归解法
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 3: return True
        def validPalindromeCore(s, left, right, deleted):
            if left == right: return True
            if left > right: return False
            if s[left] == s[right]:
                if right - left == 1: return True
                else: return validPalindromeCore(s, left + 1, right - 1, deleted)
            elif deleted:
                return False
            else:
                deleted = True
                return validPalindromeCore(s, left + 1, right, deleted) or validPalindromeCore(s, left, right - 1, deleted)
        return validPalindromeCore(s, 0, len(s) - 1, False)
        
        
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                  solution2:   迭代解法
""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if right - left < 2: return True
        if self._isValid(s, left + 1, right): return True
        if self._isValid(s, left, right - 1): return True
        return False

    def _isValid(self, s, left, right):
        return s[left:right+1] == s[left:right+1][::-1]
