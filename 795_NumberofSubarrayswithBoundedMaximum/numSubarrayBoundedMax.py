class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        sumR, sumL = 0, 0
        lastR, lastL = 0, 0
        for i in range(len(A)):
            if A[i] <= R:
                sumR += i - lastR + 1
            else:
                lastR = i + 1
            if A[i] < L:
                sumL += i - lastL + 1
            else:
                lastL = i + 1
        return sumR - sumL
