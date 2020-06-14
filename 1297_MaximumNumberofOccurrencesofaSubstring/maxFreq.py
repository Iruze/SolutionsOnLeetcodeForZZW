"""
python3, 只需记录最短的子串的个数，然后找出这里面个数的最大值即可。
因为最长的子串重复的话，那么它的子串也必然重复，故最短子串的个数 >= 最长子串的个数。
"""
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = collections.defaultdict(int)
        for i in range(len(s) - minSize + 1):
            subseq = s[i:i + minSize]
            if len(set(subseq)) <= maxLetters:
                d[subseq] += 1
        return max(d.values()) if d else 0
