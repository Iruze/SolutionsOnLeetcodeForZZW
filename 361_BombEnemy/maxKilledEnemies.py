class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        rows, cols = len(grid), len(grid[0])
        booms = [[0 for _ in range(cols)] for _ in range(rows)]
        # from rows
        for i in range(rows):
            # left -> right
            pre = 0
            for j in range(cols):
                if grid[i][j] == 'W': pre = 0
                elif grid[i][j] == 'E': pre += 1
                booms[i][j] += pre
            # right -> left
            pre = 0
            for j in range(cols - 1, -1, -1):
                if grid[i][j] == 'W': pre = 0
                elif grid[i][j] == 'E': pre += 1
                booms[i][j] += pre
        # from cols
        for j in range(cols):
            # up -> down
            pre = 0
            for i in range(rows):
                if grid[i][j] == 'W': pre = 0
                elif grid[i][j] == 'E': pre += 1
                booms[i][j] += pre
            # down -> up
            pre = 0
            for i in range(rows -1, -1, -1):
                if grid[i][j] == 'W': pre = 0
                elif grid[i][j] == 'E': pre += 1
                booms[i][j] += pre
        
        # final acculate
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    ans = max(ans, booms[i][j])
        return ans
