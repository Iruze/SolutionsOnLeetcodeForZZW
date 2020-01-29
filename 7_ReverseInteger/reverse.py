class Solution:
    def reverse(self, x: int) -> int:
        sig = '-' if x < 0 else ''
        x = str(abs(x))
        if x[0] == '0':
            x = x[1:]
        if not x:
            return 0
        x = int(x[::-1])
        if sig and x > pow(2, 31):
            return 0
        if not sig and x > pow(2, 31) - 1:
            return 0
        return x if not sig else 0 - x
