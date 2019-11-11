class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        rows, columns = len(matrix), len(matrix[0])
        row, column = rows - 1, 0
        while row >= 0 and column < columns:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                column += 1
            else:
                row -= 1
        return False
