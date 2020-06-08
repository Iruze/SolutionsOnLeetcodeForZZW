"""
python3, 动态规划：

1). dp保存了点(r, c)位置的向左，向上，向右，向下，四个方向的“臂长”；

2). 取四个方向的“臂长”作为位置(r, c)的最终阶数，在所有的阶数中取最大值即为结果
"""

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        # mine转化为结合set，能够更快的搜索
        mines_set = set()
        for r, c in mines:
            mines_set.add((r, c))
        # [左，上，右，下] 四个方向上的“臂长”
        arm = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
        ans = 0
        # 求向左，向上的“臂长”
        for r in range(N):
            for c in range(N):
                if (r, c) in mines_set: continue
                arm[r][c][0] = 1 + (arm[r][c - 1][0] if c > 0 else 0)
                arm[r][c][1] = 1 + (arm[r - 1][c][1] if r > 0 else 0)
        # 求向右，向下的臂长
        for r in range(N - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if (r, c) in mines_set: continue
                arm[r][c][2] = 1 + (arm[r][c + 1][2] if c + 1 < N else 0)
                arm[r][c][3] = 1 + (arm[r + 1][c][3] if r + 1 < N else 0)
                # 此时[r][c]的四个位置都计算完了，取最小的“臂长”作为最终的“阶数”
                # 在所有的“阶数”中取最大的那个
                ans = max(ans, min(arm[r][c]))
        return ans
        
