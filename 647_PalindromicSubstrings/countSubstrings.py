class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        s = '#' + '#'.join(s) + '#'
        maxRight, pos = 0, 0
        RL = [0] * len(s)
        for i in range(len(s)):
            if i < maxRight:
                RL[i] = min(RL[2 * pos - i], maxRight - i)
            else:
                RL[i] = 1
            while 0 <= i - RL[i] and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1
            if RL[i] - 1 + i > maxRight:
                maxRight = RL[i] - 1 + i
                pos = i
        return sum(x // 2 for x in RL)
