class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return not word
        self.length = len(word)
        def hasPathCore(row, col, depth=0):
            if self.length == depth:
                return True
            hasPath = False
            if 0 <= row and row < len(board) and \
            0 <= col and col < len(board[0]) and \
            board[row][col] == word[depth] and \
            not visited[row][col]:
                visited[row][col] = True
                up = hasPathCore(row - 1, col, depth + 1)
                down = hasPathCore(row + 1, col, depth + 1)
                left = hasPathCore(row, col - 1, depth + 1)
                right = hasPathCore(row, col + 1, depth + 1)
                hasPath = up or down or left or right
                if not hasPath:
                    visited[row][col] = False
            return hasPath
        
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if hasPathCore(i, j, 0): return True
        return False
