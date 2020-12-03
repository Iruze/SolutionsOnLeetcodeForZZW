class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(first=0, pre=[]):
            if len(pre) == k:
                ans.append(pre[:])
                return
            for i in range(first, n):
                # 这里一定是i+1, 组合数不重复
                # 组合：dfs(i + 1, pre + [nums[i]])
                # 排列: dfs(pre + [nums[i]], visited | (1 << i))
                dfs(i + 1, pre + [i + 1])
        ans = []
        dfs()
        return ans
