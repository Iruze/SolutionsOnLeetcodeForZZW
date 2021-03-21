class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        思路：如果从 source->target　能够逃出blocked的封锁，则提前终止　source->target　的搜索，证明此路可通
        　　　同理，如果 target->source　能够逃出blocked的封锁，则提前终止；
        因为如果用一般的bfs，则搜索范围为 10^6 * 10^6，　肯定超时，故想到提前"提前终止"
        ，而blocked的封锁数为: len(blocked) * (len(blocked) - 1) // 2 
        解释封锁数: len(blocked)=4, 斜对角线包围的格子数=1+2+3+4
        """
        if not blocked:
            return True
        blocked = set([(x, y) for x, y in blocked])
        # source->target 和 target->source 两条路都能够“提前终止”，则证明最终结果能通
        source_to_target = Solution._bfs(source, target, blocked)
        target_to_source = Solution._bfs(target, source, blocked)
        return source_to_target and target_to_source
    
    @staticmethod
    def _bfs(start, end, blocked):
        blocked_steps = 1
        walked = set([(start[0], start[1])])
        queue = collections.deque([(start[0], start[1])])
        while queue:
            # 超出blocked的封锁数，证明能够逃出封锁
            if blocked_steps > len(blocked) * (len(blocked) - 1) // 2:
                return True
            x, y = queue.popleft()
            # 直接访问到了终点
            if [x, y] == end:
                return True
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                #　(x, y)搜索附近能够到达的相邻网格(nx, ny)
                if 0 <= nx < 10 ** 6 and 0 <= ny < 10 ** 6 and (nx, ny) not in walked and (nx, ny) not in blocked:
                    blocked_steps += 1
                    walked.add((nx, ny))
                    queue.append((nx, ny))
        return False
