class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(r, c):
            m, n = 9, 9
            # base case
            if r == m:
                return True
            if c == n:
                return backtrack(r + 1, 0)
            for i in range(r, m):
                for j in range(c, n):
                    # 当前格子是数字，直接递归到下一个格子
                    if board[i][j] != '.':
                        return backtrack(i, j + 1)
                    # 挨个数字尝试，不符合的continue
                    # 这点不同于上面的继续递归，这里是针对一个格子枚举，不符合即跳过
                    # 上面则是，没有触发到base case，则继续下一个递归链
                    for ch in map(str, range(1, 10)):
                        if not isValid(i, j, ch):
                            continue
                        board[i][j] = ch
                        # 符合要求的数字，保存结果，无需恢复'.'
                        if backtrack(i, j + 1):
                            return True
                        board[i][j] = '.'
                    # 枚举遍了0-9还是没有结果，返回false
                    return False
            return False
        
        def isValid(r, c, ch):
            for i in range(9):
                # 同行
                if board[r][i] == ch: return False
                # 同列
                if board[i][c] == ch: return False
                # 同一个小9格子
                if board[(r//3)*3 + i//3][(c//3)*3 + i % 3] == ch: return False
            return True
        
        backtrack(0, 0)
