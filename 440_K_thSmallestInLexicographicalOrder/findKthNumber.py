"""
参考：
1. https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/solution/ben-ti-shi-shang-zui-wan-zheng-ju-ti-de-shou-mo-sh/
2. https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/solution/shi-cha-shu-by-powcai/
"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getCount(prefix, n):
            cur, nxt = prefix, prefix + 1
            count = 0
            while cur <= n:
                count += min(nxt, n + 1) - cur
                nxt, cur = nxt * 10, cur * 10
            return count
        p = 1
        prefix = 1
        while p < k:
            count = getCount(prefix, n)
            if p + count > k:
                prefix *= 10
                p += 1
            else:
                prefix += 1
                p += count
        return prefix
        
