class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows, columns = len(A), len(A[0])
        output = [[0] * rows for _ in range(columns)]
        for i in range(rows):
            for j in range(columns):
                output[j][i] = A[i][j]
        return output
