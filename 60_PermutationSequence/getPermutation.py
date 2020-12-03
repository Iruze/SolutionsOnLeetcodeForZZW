class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        比如在1234中找第 9 个数：‘2314’
        """
        def dfs(n, k, pre=[], depth=0):
            if depth == n:
                return ''.join(pre)
            # 以depth=0为例，此时以1为前缀的数有 (4-1)! 个
            ps = count(n - 1 - depth)
            for i in range(n):
                if not visited[i]:
                    # 3! < 9，说明肯定不是以1为前缀，从1后面的234中重新选
                    if ps < k:
                        # 去掉了以1为前缀的分支，那个分支共有 3! 个数
                        k -= ps
                        continue
                    # 是当前的2为前缀的分支, 加入结果集，当前层over
                    pre.append(str(i + 1))
                    visited[i] = True
                    # 下一层递归
                    return dfs(n, k, pre, depth + 1)
        # 尾递归求 n!
        def count(n, res=1):
            return res if n == 0 or n == 1 else count(n - 1, res * n)
        
        visited = [False for _ in range(n)]
        return dfs(n, k)

    
    
    
# 利用 math.factorial() 函数的写法
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n, k, cur=[], depth=0, visited=0):
            if depth == n:
                return ''.join(cur)
            for i in range(n):
                if visited & (1 << i) == 0:
                    ps = math.factorial(n - 1 - depth)
                    if ps < k:
                        k -= ps
                        continue
                    cur.append(str(i + 1))
                    return dfs(n, k, cur, depth + 1, visited | (1 << i))
        return dfs(n, k)
