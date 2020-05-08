"""
python3, BFS搜索，相当于二叉树的层次遍历：
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # 类似于二叉树的层次遍历，结果存在某一层
        visited = [False for _ in range(len(arr))]
        visited[0] = True
        # 存储arr中值对应的所有索引
        d = collections.defaultdict(list)
        for i, v in enumerate(arr):
            d[v].append(i)
        # cur, nxt 分别表示当前层，和下一层
        cur, nxt = [], []
        cur.append(0)
        step = 0
        while cur:
            step += 1
            for i in cur:
                if i == len(arr) - 1:
                    return step - 1
                # 前一个索引
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    nxt.append(i - 1)
                # 后一个索引
                if i + 1 < len(arr) and not visited[i + 1]:
                    visited[i + 1] = True
                    nxt.append(i + 1)
                # 值相同的所有索引
                for idx in d[arr[i]]:
                    if not visited[idx]:
                        visited[idx] = True
                        nxt.append(idx)
                # 虽然上面的for里面visited[idx]使得下一个的idx不会在搜索
                #， 但是对于[7,7,7,...,7]这种很长的arr，
                # 上面的for idx in d[arr[i]]还是会停留很久，相当于sleep，
                # ， 索性在d[arr[i]]访问后，直接令arr[i]其他的索引为空
                d[arr[i]] = []
            cur, nxt = nxt, []
        return len(arr)
