class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0: return []
        start = 0
        output = [[0] * n for _ in range(n)]
        f = self.__nextNumOfpow2(n)
        while start < n:
            self.__generateMatrixCore(n, n, output, start, f)
            start += 1
        return output
    
    
    def __generateMatrixCore(self, rows, columns, output, start, f):
        endX = columns - 1 - start
        endY = rows - 1 - start
        
        # left -> right
        for i in range(start, endX + 1):
            output[start][i] = next(f)
        
        # up -> down
        if endY > start:
            for i in range(start + 1, endY + 1):
                output[i][endX] = next(f)
        
        # right -> left
        if endY > start and endX > start:
            for i in range(endX - 1, start - 1, -1):
                output[endY][i] = next(f)
        
        # down -> up
        if endX > start and endY - start > 1:
            for i in range(endY - 1, start, -1):
                output[i][start] = next(f)
    
    
    def __nextNumOfpow2(self, n):
        ans = 1
        while ans <= n ** 2:
            yield ans
            ans += 1
        return
        
