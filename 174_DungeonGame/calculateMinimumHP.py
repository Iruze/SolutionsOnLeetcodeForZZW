class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[0] * cols for _ in range(rows)]
        # dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        # for r in range(rows - 1, -1, -1):
        #     for c in range(cols - 1, -1, -1):
        #         if r == rows - 1 and c == cols - 1: 
        #             continue
        #         elif r == rows - 1:
        #             dp[r][c] = max(1, dp[r][c + 1] - dungeon[r][c])
        #         elif c == cols - 1:
        #             dp[r][c] = max(1, dp[r + 1][c] - dungeon[r][c])
        #         else:
        #             dp[r][c] = max(1, min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c])
        # return dp[0][0]
        import functools
        @functools.lru_cache(None)
        def helper(r, c):
            if r == rows - 1 and c == cols - 1:
                return max(1, 1 - dungeon[-1][-1])
            if r == rows - 1:
                return max(1, helper(r, c + 1) - dungeon[r][c])
            if c == cols - 1:
                return max(1, helper(r + 1, c) - dungeon[r][c])
            return max(1, min(helper(r + 1, c), helper(r, c + 1)) - dungeon[r][c])
        return helper(0, 0)
