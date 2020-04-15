class Solution:
    def checkValidString(self, s: str) -> bool:
        # lo_min和lo_max分别记录左括号的最大个数和最小个数
        lo_min, lo_max = 0, 0
        for c in s:
            if c == '(':
                lo_min += 1
                lo_max += 1
            elif c == '*':
                if lo_min > 0:
                    lo_min -= 1
                lo_max += 1
            else:
                if lo_min > 0:
                    lo_min -= 1
                lo_max -= 1
            if lo_max < 0:
                return False
        return lo_min == 0
