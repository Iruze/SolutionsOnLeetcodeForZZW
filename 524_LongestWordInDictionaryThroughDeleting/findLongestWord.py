class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for c in d:
            # 比给定字符串还长，肯定不能通过删除得到
            if len(c) > len(s):
                continue
            if self.hasSubseq(c, s):
                return c
        return ''
    
    # 判定s1是否是s2的子序列，len(s1) < len(s2)
    def hasSubseq(self, s1, s2):
        i1, i2 = 0, 0
        while i1 < len(s1) and i2 < len(s2):
            if s1[i1] == s2[i2]:
                i1 += 1
            i2 += 1
        return i1 == len(s1)
