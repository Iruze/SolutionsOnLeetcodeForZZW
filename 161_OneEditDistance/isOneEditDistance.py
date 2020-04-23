# 方法一： 递归
class Solution:

    edited = False

    def isOneEditDistance(self, s: str, t: str) -> bool:
        # base case
        if not s:
            return len(t) == 0 if self.edited else len(t) == 1
        if not t:
            return len(s) == 0 if self.edited else len(s) == 1
        # 相等，直接下一轮比较
        if s[0] == t[0]:
            return self.isOneEditDistance(s[1:], t[1:])
        # 还不相等，但已经用完了编辑的唯一一次机会
        elif self.edited:
            return False
       # 机会还没用，此时编辑
        else:
            self.edited = True
            # 分三种情况编辑
            return self.isOneEditDistance(s, t[1:]) or self.isOneEditDistance(s[1:], t) or self.isOneEditDistance(s[1:], t[1:])
