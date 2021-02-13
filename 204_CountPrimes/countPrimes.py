class Solution:
    def countPrimes(self, n: int) -> int:
        # 埃氏筛选法
        prime = [True] * n
        for i in range(2, n):
            if prime[i]:
                #  本来是从 i * 2开始的，但是以2-i之间的质数为因数的数早就被筛掉了
                # ， 做个优化， 直接从 i ** 2开始即可
                for j in range(i ** 2, n, i):
                    prime[j] = False
        return sum(prime[2:])
