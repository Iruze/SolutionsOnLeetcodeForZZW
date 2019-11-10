class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = -float('inf')
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    for r in range(rows):
                        if matrix[r][j] != 0: matrix[r][j] = MODIFIED
                    for c in range(columns):
                        if matrix[i][c] != 0: matrix[i][c] = MODIFIED
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == MODIFIED:
                    matrix[i][j] = 0
