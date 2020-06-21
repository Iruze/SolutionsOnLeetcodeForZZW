# 方法一：　递归
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 3 or n == 1: return True
        if n < 3 or n % 3 != 0: return False
        if n ** 0.5 == 0:
            return self.isPowerOfThree(n ** 0.5)
        else:
            return self.isPowerOfThree(n // 3)
            
            
# 方法二：　换底公式
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        ans = math.log(n) / math.log(3)
        return ans - int(ans) == 0 or abs(1 - ans + int(ans)) < 10e-12
