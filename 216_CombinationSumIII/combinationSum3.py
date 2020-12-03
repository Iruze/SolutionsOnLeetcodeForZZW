# 回溯 + DFS
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(first=1):
            if len(cur) == k:           # 回溯结束条件
                if sum(cur) == n:
                    ans.append(cur[:])  # 注意：浅拷贝cur，不然后面 cur.pop 最后得到的是空[]
                else:
                    return
            for i in range(first, 10):
                cur.append(i)
                dfs(i + 1)              # DFS
                cur.pop()               # 弹出使用的 i，回溯
        cur, ans = [], []
        dfs()
        return ans

    
    
# 回溯的快速写法
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(n, k, first=1, pre=[]):
            if len(pre) == k:
                if sum(pre) == n:
                    ans.append(pre[:])
                return
            for i in range(first, 10):
                dfs(n, k, i + 1, pre + [i])
        dfs(n, k)
        return ans
