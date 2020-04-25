"""
参考了：
https://leetcode-cn.com/problems/lexicographical-numbers/solution/zi-fu-chuan-pai-xu-dfs-by-powcai/
"""

# 解法一：字符串排序
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=str)


# 解法二：dfs
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(prefix):
            if prefix > n:
                return
            ans.append(prefix)
            for i in range(10):
                dfs(prefix * 10 + i)
        
        for prefix in range(1, 10):
            dfs(prefix)
        return ans
        
