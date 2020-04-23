class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[:][::-1]
        lo = 0
        for hi in range(len(s) + 1):
            # or 前后这两个项位置不要调换
            if hi == len(s) or s[hi] == ' ':
                s[lo:hi] = s[lo:hi][::-1]
                lo = hi + 1
