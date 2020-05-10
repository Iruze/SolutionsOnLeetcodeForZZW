class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        rows, cols = len(board), len(board[0])
        start = tuple(itertools.chain(*board))
        # 想象成二叉树的层次遍历，将当前所有可能的交换状态入队，逐层搜索直到(1, 2, 3, 4, 5, 0)
        deque = collections.deque([(start, start.index(0), 0)])
        # tuple的hash效率比较高，故将状态转化为tuple存储
        visited = {start}
        target = tuple([*range(1, rows * cols)] + [0])
        
        while deque:
            cur, pos, steps = deque.popleft()
            if cur == target:
                return steps
            # 可交换的位置：同一行的左右，或者同一列的上下
            for offset in (-1, 1, cols, -cols):
                new_pos = pos + offset
                # 排除掉二维上 <第一行的行尾和第二行的行首> 这类不可能的交换
                if abs(pos//cols - new_pos//cols) + abs(pos%cols - new_pos%cols) != 1:
                    continue
                # 必须在一维长度区间内交换
                if 0 <= new_pos < rows * cols:
                    # 新建可能的下一个状态
                    nxt = list(cur)
                    nxt[pos], nxt[new_pos] = nxt[new_pos], nxt[pos]
                    nxt = tuple(nxt)
                    if nxt not in visited:
                        visited.add(nxt)
                        deque.append((nxt, new_pos, steps + 1))
        return -1
