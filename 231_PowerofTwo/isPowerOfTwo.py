# 方法一：　递归
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1 or n == 2: return True
        if n % 2 != 0: return False
        if n ** 0.5 != 0:
            return self.isPowerOfTwo(n // 2)
        else:
            return self.isPowerOfTwo(n ** 0.5)

＃ 方法二：　位运算
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        # 2的整数次幂只有一个１
        return n & (n - 1) == 0
