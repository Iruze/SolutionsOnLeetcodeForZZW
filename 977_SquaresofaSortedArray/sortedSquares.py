# 方法一: O(nlongn)，平方＋排序

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([*map(lambda x: x ** 2, A)])
        
        
        
        
# 方法二: O(n)，平方＋中间向两边归并

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A[0] >= 0:
            return [*map(lambda x: x ** 2, A)]
        if A[-1] <= 0:
            return [*map(lambda x: x ** 2, A)][::-1]
        ans = [0 for _ in range(len(A))]
        for idx, a in enumerate(A):
            if a >= 0:
                break
        A = [*map(lambda x: x ** 2, A)]
        m, n = idx - 1, idx
        t = 0
        while m >= 0 and n < len(A):
            if A[m] < A[n]:
                ans[t] = A[m]
                m -= 1
            else:
                ans[t] = A[n]
                n += 1
            t += 1
        while m >= 0:
            ans[t] = A[m]
            t, m = t + 1, m - 1
        while n < len(A):
            ans[t] = A[n]
            t, n = t + 1, n + 1
        return ans
