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

# python, dfs解法
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, word, visited=set()):
            # Base case
            if not word:
                return True
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                # 搜索相邻的，且没有被访问过的位置
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    # 这个位置字符和word开头对上了
                    if board[ni][nj] == word[0]:
                        # 在下一层中，找到了一个成功的方向，即刻返回true
                        if dfs(ni, nj, word[1:], visited | {(ni, nj)}):
                            return True
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # 开头对上了，进入下一层寻找
                if board[i][j] == word[0]:
                    # 剩下的依然匹配，则返回true
                    if dfs(i, j, word[1:], set([(i, j)])):
                        return True
        return False
