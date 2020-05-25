"""
贪心思想：

归类：这题和下面这两道题思路几乎一模一样：

[435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)

[452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons)
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        count = 0
        end = -float('inf')
        for i, p in enumerate(pairs):
            if p[0] > end:
                count += 1
                end = p[1]
        return count        
