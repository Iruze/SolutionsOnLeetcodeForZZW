class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m: return False
        elif m == 1: return target in matrix[0]
        n = len(matrix[0])
        if target < matrix[0][0] or matrix[m - 1][n - 1] < target:
            return False
        
        startC, endC = 0, m - 1
        while startC < endC:
            midC = (startC + endC) // 2
            if target <= matrix[midC][-1]:
                endC = midC
            elif matrix[midC][-1] < target:
                startC = midC + 1
        
        startR, endR = 0, n - 1
        while startR < endR:
            midR = (startR + endR) // 2
            if matrix[startC][midR] == target:
                return True
            elif matrix[startC][midR] < target:
                startR = midR + 1
            else:
                endR = midR
        return matrix[startC][startR] == target
