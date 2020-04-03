# 方法pro: O(logmn)的二分法
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        if target < matrix[0][0] or target > matrix[-1][-1]: return False
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            r, c = mid // cols, mid % cols
            if matrix[r][c] < target:
                lo = mid + 1
            else:
                hi = mid
        return matrix[lo // cols][lo % cols] == target
    
    
# 方法一： 二分法-传统流程 O(logm * logn)
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

# 方法二： 二分法-借用bisect，numpy.array()函数, O(logm * logn)
import numpy as np

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        rows, cols = len(matrix), len(matrix[0])
        mat = np.array(matrix)
        # 找到应该插入的行
        r = bisect.bisect_left(mat[:, cols - 1], target)
        # 如果插入在行尾，则说明target大于行尾的数，
        if r >= rows: return False
        if matrix[r][-1] == target: return True
        # 找到应该插入的列
        c = bisect.bisect_left(matrix[r], target)
        return matrix[r][c] == target
