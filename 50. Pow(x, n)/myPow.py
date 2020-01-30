# 解法一： 递归版本
# 时间O(logN), 空间O(logN)
"""
递归基础条件：
1). n = 1：返回x
2). n为奇数，则x*myPow(x, n - 1)
3). n为偶数， 则 myPow(x, n // 2) ** 2
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        if n == 1:
            return x
        if n < 0:
            x = 1 / x
            n = - n
        if n & 1:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x, n // 2) ** 2
            
# 解法二： 迭代法
# 时间O(logN), 空间O(logN)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = - n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
