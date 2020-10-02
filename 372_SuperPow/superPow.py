class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        base = 1337
        # 50. Pow(x, n)的写法
        def _myPow(x, n):
            ans = 1
            while n:
                if n & 1 == 1:
                    ans = ans * x % base
                x = x ** 2 % base
                n >>= 1
            return ans
        
        if not b:
            return 1
        # 幂运算公式: (x, 1234) = ((x, 123), 10) * (x, 4)
        last = b.pop()
        part1 = _myPow(a, last)
        part2 = _myPow(self.superPow(a, b), 10)
        return part1 * part2 % base
