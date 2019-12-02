class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        x = str(x)
        return x == x[::-1] and x[::-1][0] != '0'
