class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if len(A) < 2:
            return -1
        A.sort()
        if A[0] + A[1] >= K:
            return -1
        # 首尾双指针
        left, right = 0, len(A) - 1
        res = -float('Inf')
        # 最终 left = right，但是不影响res
        while left < right:
            S = A[left] + A[right]
            if S < K:
                res = max(res, S)
                left += 1
            else:
                right -= 1
        return res
