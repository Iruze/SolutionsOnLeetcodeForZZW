# 方法一： 枚举法， 枚举 str2的2，3，...，等分得到的除数div
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 判断div是否是s的除数
        def _isDivisor(s, div):
            if not s: return True
            return s.startswith(div) and _isDivisor(s[len(div):], div)
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        n1, n2 = len(str1), len(str2)
        # 枚举法： 枚举短字符串str2的2，3，...，len(str2)等分
        for ln in range(1, n2 + 1):
            if n2 % ln == 0:
                wd = n2 // ln
                # 将str2的wd等分
                div = str2[:wd]
                if _isDivisor(str1, div) and _isDivisor(str2, div):
                    return div
        return ""
        
        
# 方法二：数学法
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ln = math.gcd(len(str1), len(str2))
        candidate = str1[:ln]
        if str1 + str2 == str2 + str1:
            return candidate
        return ''
