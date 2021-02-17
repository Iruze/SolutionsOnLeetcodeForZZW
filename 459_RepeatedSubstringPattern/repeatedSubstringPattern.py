class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
        
        
# 参考：
# https://leetcode-cn.com/problems/repeated-substring-pattern/solution/gou-zao-shuang-bei-zi-fu-chuan-by-elevenxx/
