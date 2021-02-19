# 方法一: 记忆化递归
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @functools.lru_cache(None)
        def helper(s):
            if not s: return 1
            if s[0] == '0': return 0
            if len(s) > 1 and s[:2] <= '26':
                return helper(s[1:]) + helper(s[2:])
            return helper(s[1:])
        
        return helper(s)
    
# 方法二: 青蛙跳台阶解法
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        f1, f2, f = 1, 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] in {'1', '2'}:
                    f = f1
                else:
                    return 0
            elif s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
                f = f1 + f2
            f1, f2 = f2, f
        return f
