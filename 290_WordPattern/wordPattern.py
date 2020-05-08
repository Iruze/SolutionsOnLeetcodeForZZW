"""
解法一：
python3, 比较pattern和str的字符映射位置：
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        string = str.split(' ')
        if len(pattern) != len(string):
            return False
        d1, d2 = dict(), dict()
        for i, v in enumerate(string):
            if pattern[i] not in d1:
                if v in d2: return False      # pattern[i]以前没出现过，而string[i]以前却出现过
                d1[pattern[i]] = i               # 记下pattern[i]首次出现的位置
                d2[v] = i                           # 记下string[i]首次出现的位置
            # pattern[i]以前出现过，而string[i]没出现过；或者都出过，但是位置不一样
            elif v not in d2 or d1[pattern[i]] != d2[v]:  
                return False
        return True
        
# 解法二：

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        res = str.split(' ')
        return [*map(pattern.index, pattern)] == [*map(res.index, res)] 
