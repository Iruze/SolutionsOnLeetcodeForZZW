# 参考： https://leetcode-cn.com/problems/divide-two-integers/solution/po-su-de-xiang-fa-mei-you-wei-yun-suan-mei-you-yi-/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 以 11 / 3为例
        def div(a, b):
            if a < b:
                return 0
            tb = b
            # 11 > 3， 肯定至少为1
            count = 1
            # 3 + 3 <= 11
            while tb + tb <= a:
                count = count + count          # 至少为 1+1
                tb = tb + tb                   # 3变为6
            return count + div(a - tb, b)      # 结果为2 + div(11-6, 3)
        if divisor == 1: 
            return dividend
        elif divisor == -1: 
            return min(-dividend, pow(2, 31) - 1)
        sign = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = -1
        # div(a, b)函数中a, b均为正整数
        dividend = abs(dividend)
        divisor = abs(divisor)
        return sign * div(dividend, divisor)
