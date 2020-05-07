import math


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # 本身算一个
        ans = 1
        # 由等差公式 Sn = n*a1 + n*(n - 1)/2 得到：
        # 1. Sn >= n*n / 2, 即 n <= sqrt(Sn*2)
        # 2. a1 = (Sn -n*(n - 1)/2) / n ]]， a1得是整数
        for n in range(2, math.floor((2 * N) ** 0.5) + 1):
            if (N - n * (n - 1) // 2) % n == 0:
                ans += 1
        return ans
