class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        # A有序
        @functools.lru_cache(None)
        def dfs(begin, size, target):
            # base case
            if size == 0:
                return target == 0
            # 不可能存在
            if A[begin] * size > target:
                return False
            for i in range(begin, len(A) - size + 1):
                # 避免重复的数作为第一个数
                if i > begin and A[i] == A[i - 1]:
                    continue
                if dfs(i + 1, size - 1, target - A[i]):
                    return True
            return False

        A.sort()
        n, SUM = len(A), sum(A)
        # A分为两个数组，一长一短，寻找短的那个数组即可
        for i in range(1, n//2 + 1):
            # sum1 = sum * i / N, 利用sum1为整数剪枝
            if SUM * i % n == 0 and dfs(0, i, SUM * i // n):
                return True
        return False
