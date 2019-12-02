class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'
        RL = [0] * len(s)
        maxRight, pos = 0, 0
        res = ''
        for i in range(len(s)):
            if i < maxRight:
                RL[i] = min(RL[2 * pos - i], maxRight - i)
            else:
                RL[i] = 1
            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1
            if RL[i] - 1 + i > maxRight:
                maxRight = RL[i] - 1 + i
                pos = i
            if RL[i] - 1 > len(res):
                res = s[i-RL[i]+1:i+RL[i]].replace('#', '')
        return res
