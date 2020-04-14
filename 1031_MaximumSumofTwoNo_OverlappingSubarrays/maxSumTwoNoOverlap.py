class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + A[i - 1]
        ans = 0
        for _ in range(2):
            maxLeft = 0
            for i in range(L, len(presum) - M):
                maxLeft = max(maxLeft, presum[i] - presum[i - L])
                ans = max(ans, maxLeft + (presum[i + M] - presum[i]))
            L, M = M, L
        return ans
