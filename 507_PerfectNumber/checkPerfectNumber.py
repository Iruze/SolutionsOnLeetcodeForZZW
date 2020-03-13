class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 负数和奇数都不是完美数
        if num < 0 or num & 1 != 0:
            return False
        SUM = 1
        sqrt = math.floor(math.sqrt(num))
        for i in range(2, sqrt + 1):
            if num % i == 0:
                SUM += i + num // i
        # 当num正好可以开平方，SUM加了两次sqrt，故要回退
        if sqrt ** 2 == num:
            SUM -= sqrt
        return SUM == num
