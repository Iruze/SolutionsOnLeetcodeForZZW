class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rows = cols = 8
        for r in range(rows):
            if 'R' in board[r]:
                c = board[r].index('R')
                break
        ans = 0
        # East: c - > cols
        for e in range(c + 1, cols):
            if board[r][e] is 'B': break
            if board[r][e] is 'p': ans += 1; break
        # West: c - > 0
        for w in range(c - 1, -1, -1):
            if board[r][w] is 'B': break
            if board[r][w] is 'p': ans += 1; break
        # North: r -> 0
        for n in range(r - 1, -1, -1):
            if board[n][c] is 'B': break
            if board[n][c] is 'p': ans += 1; break
        # South: r - > rows
        for s in range(r + 1, cols):
            if board[s][c] is 'B': break
            if board[s][c] is 'p': ans += 1; break
        return ans
