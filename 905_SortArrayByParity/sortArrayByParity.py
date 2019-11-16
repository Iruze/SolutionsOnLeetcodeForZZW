class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A: return []
        left, right = 0, len(A) - 1
        while left < right:
            while A[left] % 2 == 0 and left < right:
                left += 1
            while A[right] % 2 == 1 and left < right:
                right -= 1
            if left < right:
                A[left], A[right] = A[right], A[left]
        return A
