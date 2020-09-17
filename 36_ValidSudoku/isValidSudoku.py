class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # def valid(r, c):
        #     for i in range(9):
        #         # 同行是否重复
        #         if i != c and board[r][i] == board[r][c]: return False
        #         # 同列是否重复
        #         if i != r and board[i][c] == board[r][c]: return False
        #         r1 = (r // 3) * 3 + i // 3
        #         c1 = (c // 3) * 3 + i % 3
        #         # 小9宫格是否重复
        #         if r1 != r and c1 != c and board[r1][c1] == board[r][c]:
        #             return False
        #     return True
        
        # for r in range(9):
        #     for c in range(9):
        #         # 只检查非空格子
        #         if board[r][c] != '.' and  not valid(r, c):
        #             return False
        # return True

        # 记录第i行 0-9 的数字各自是否之前出现
        rows = {i: [False] * 10 for i in range(9)}
        # 第j列
        cols = {j: [False] * 10 for j in range(9)}
        # 第 (i1, j1) 个box
        boxes = {(i, j):[False] * 10 for i in range(3) for j in range(3)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    # 第i行, 或第j列, 或小的3*3宫格 重复
                    if rows[i][num] or cols[j][num] or boxes[(i // 3, j // 3)][num]:
                        return False
                    # 此时第i行, 第j列, 第(i1, j1)宫格都出现了数字num, 这三个域都要记录
                    rows[i][num] = cols[j][num] = boxes[(i // 3, j // 3)][num] = True
        return True
