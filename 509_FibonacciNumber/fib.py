class Solution:
    def fib(self, N: int) -> int:
        f1, f2 = 0, 1
        for i in range(N):
            f1, f2 = f2, f1 + f2
        return f1
