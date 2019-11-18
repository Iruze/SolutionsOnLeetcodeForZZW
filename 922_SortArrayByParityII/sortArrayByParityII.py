class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        A[::2], A[1::2] = [i for i in A if i % 2 == 0], [j for j in A if j % 2 == 1]
        return A
