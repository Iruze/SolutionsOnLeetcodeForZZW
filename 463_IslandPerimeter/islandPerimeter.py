class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        totalper = 0
        island, rightedg, downedg = 0, 0, 0
        rows, cols = len(grid), len(grid[0])
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    island += 1
                    if c + 1 < cols and grid[r][c + 1] == 1:
                        rightedg += 1
                    if r + 1 < rows and grid[r + 1][c] == 1:
                        downedg += 1
        return island * 4 - 2 * (rightedg + downedg)
