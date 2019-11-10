class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        output = []
        start = 0
        rows, columns = len(matrix), len(matrix[0])
        while start * 2 < rows and start * 2 < columns:
            self.__spiralOrderCore(matrix, rows, columns, start, output)
            start += 1
        return output
    
    
    def __spiralOrderCore(self, matrix, rows, columns, start, output):
        endX = columns - 1 - start
        endY = rows - 1 - start
        
        # left -> right
        for i in range(start, endX + 1):
            output.append(matrix[start][i])
        
        # up -> down
        if start < endY:
            for i in range(start + 1, endY + 1):
                output.append(matrix[i][endX])
        
        # right -> left
        if endY - start > 0 and endX - start > 0:
            for i in range(endX - 1, start - 1, -1):
                output.append(matrix[endY][i])
        
        # down -> up
        if endY - start > 1 and endX - start > 0:
            for i in range(endY - 1, start, -1):
                output.append(matrix[i][start])
