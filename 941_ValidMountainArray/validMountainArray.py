class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3: return False
        left, right = 0, n - 1
        while left < n - 1 and A[left] < A[left + 1]:
            left += 1
        if left == n - 1 or not left: return False
        while right > 0 and A[right - 1] > A[right]:
            right -= 1
        return left == right
