"""
类似于前缀和，求完所有的[0, 0]-[i, j]矩形上的总和：则

result = SUM([0, 0]-[row2, col2]) - SUM([0, 0] - [row1 - 1, col2]) - SUM([0, 0] - [row2, col1 - 1]) + SUM([0, 0] - [row1 - 1, col1 - 1])
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.matrix = matrix
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0: continue
                # 右上区域
                if r == 0: self.matrix[r][c] += self.matrix[r][c - 1]
                # 左下区域
                if c == 0: self.matrix[r][c] += self.matrix[r - 1][c]
                # 左上公共区域， [0, 0] - [row1 - 1, col1 - 1] 是公共区域，被减了两次，故要加一次回来
                if r > 0 and c > 0: self.matrix[r][c] += self.matrix[r - 1][c] + self.matrix[r][c - 1] - self.matrix[r - 1][c - 1]
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 右上
        hi_up = self.matrix[row1 - 1][col2] if row1 > 0 else 0
        # 左下
        lo_down = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        # 左上
        lo_up = self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.matrix[row2][col2] - hi_up - lo_down + lo_up
