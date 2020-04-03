# 方法一：
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int('1' * (len(bin(N)) - 2), 2) - N
        
# 方法二：
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        ans, cnt = 0, 0
        for i in range(31, -1, -1):
            if N & (1 << i):       # 记录首个非0前缀的开始
                cnt += 1
            if cnt >= 1 and not N & (1 << i):
                ans |= (1 << i)
        return ans
