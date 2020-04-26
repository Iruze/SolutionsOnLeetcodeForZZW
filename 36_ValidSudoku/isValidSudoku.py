class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                # 只检查非空格子
                if board[r][c] != '.' and  not self.isValid(board, r, c):
                    return False
        return True
    
    def isValid(self, board, r, c):
        for i in range(9):
            # 同行是否重复
            if i != c and board[r][i] == board[r][c]: return False
            # 同列是否重复
            if i != r and board[i][c] == board[r][c]: return False
            r1 = (r // 3) * 3 + i // 3
            c1 = (c // 3) * 3 + i % 3
            # 小9宫格是否重复
            if r1 != r and c1 != c and board[r1][c1] == board[r][c]:
                return False
        return True
