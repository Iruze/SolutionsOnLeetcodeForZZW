"""
1. 既然是只能从s前面插入字符串使之回文，那原始的s不是回文的时候，s前面插入的一定是s后面若干字符的翻转（对称性）；
2. 假设s[0:i]还是回文串，所以右指针hi从s末尾向s头移动，寻找回文的s[:i]，剩下需要插入的就是把s[i+1:]反转一下，插到s的头就行啦：
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        hi = len(s)
        while hi > 0:
            if s[:hi] == s[:hi][::-1]:
                break
            hi -= 1
        return s[hi:][::-1] + s
