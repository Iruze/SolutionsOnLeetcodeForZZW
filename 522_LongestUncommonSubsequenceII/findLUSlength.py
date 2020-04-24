"""
1. 先根据字符长度逆序排序，最长的字符排在前面；
2. 关注出现一次的字符，如果该字符不是前面所有字符的子序列，则它是最长的特殊字符
"""

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # 特殊字符如果存在，则肯定是strs中某一个字符
        # 则从最长的字符开始寻找
        s = Counter(strs)
        count = sorted([*zip(s.keys(), s.values())], key=lambda x: len(x[0]), reverse=True)
        # 存下出现过的不是最长子序列的长字符
        pre = set()
        # 只找出现一次的
        for k, v in count:
            if v == 1:
                for p in pre:
                    # 虽然出现一次，但是是前面字符的子序列
                    if self.isSubseq(k, p):
                        break
                # 都不是前面字符的子序列
                else:
                    return len(k)
            else:
                pre.add(k)
        return -1
    
    # 检测s1是否是s2的子序列，len(s1) <= len(s2)
    def isSubseq(self, s1, s2):
        l1, l2 = 0, 0
        while l1 < len(s1) and l2 < len(s2):
            if s1[l1] == s2[l2]:
                l1 += 1
            l2 += 1
        return l1 == len(s1)
