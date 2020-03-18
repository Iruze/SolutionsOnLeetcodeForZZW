class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        # 对于 24 这种，只需要计数 
        # 对于 25 // 5 // 5 的情况，需要 n //= 5 来除尽
        while n >= 5:
            n //= 5
            res += n
        return res
