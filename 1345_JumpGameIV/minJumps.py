"""
python3, BFS搜索，相当于二叉树的层次遍历：
"""

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # 每个arr[i]值对应的所有索引位置
        pos = collections.defaultdict(list)
        for idx, num in enumerate(arr):
            pos[num].append(idx)
        deque = collections.deque([(0, 0)])
        visited = set([0])
        while deque:
            idx, step = deque.popleft()
            # 结束
            if idx == len(arr) - 1:
                return step
            # i + 1跳
            if idx + 1 < len(arr) and idx + 1 not in visited:
                visited.add(idx + 1)
                deque.append((idx + 1, step + 1))
            # i - 1跳
            if idx - 1 >= 0 and idx - 1 not in visited:
                visited.add(idx - 1)
                deque.append((idx - 1, step + 1))
            # 所有值相同的跳
            for nxt in pos[arr[idx]]:
                if nxt not in visited:
                    visited.add(nxt)
                    deque.append((nxt, step + 1))
            """虽然上面的for里面visited[idx]使得下一个的idx不会在搜索
            但是对于[7,7,7,...,7]这种很长的arr，
            上面的for idx in d[arr[i]]还是会停留很久，相当于sleep，
            索性在d[arr[i]]访问后，直接令arr[i]其他的索引为空"""
            pos[arr[idx]] = []
        return -1
