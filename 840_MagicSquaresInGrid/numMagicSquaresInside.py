class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # 空矩阵，退出
        if not grid or not grid[0]: 
            return 0
        rows, columns = len(grid), len(grid[0])
        # 维度小于3， 退出
        if rows < 3 or columns < 3: 
            return 0
        count = 0
        # 以左上点出发，全局搜索[0, rows - 3], [0, columns - 3]
        for i in range(rows - 2):
            for j in range(columns - 2):
                # 判断是否为幻方
                if self.__validMagicSquare(grid, i, j):
                    count += 1
        return count
    
    
    def __validMagicSquare(self, grid, row, column):
        # 第一部分：3维幻方，中间必=5
        if grid[row + 1][column + 1] != 5:
            return False
        # 第二部分： 判断是否属于[0, 9]，且不重复
        s = set()
        for i in range(3):
            for j in range(3):
                t = grid[row + i][column + j]
                # t在[0, 9]之间，且不重复
                if t in s or t < 1 or t > 9:
                    return False
                else:
                    s.add(grid[row + i][column + j])
        # 第三部分：判断所有的行列的和是否相等，无需判断对角线足以
        for i in range(3):
            sumRow, sumCol = 0, 0
            for j in range(3):
                sumRow += grid[row + i][column + j]
                sumCol += grid[row + j][column + i]
            #  3维幻方的行列和=15
            if sumRow != 15 or sumCol != 15:
                return False
        return True
        
