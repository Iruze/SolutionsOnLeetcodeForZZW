"""
参考：
https://leetcode-cn.com/problems/maximum-of-absolute-value-expression/solution/man-ha-dun-ju-chi-python3-by-smoon1989/
"""
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = float('-Inf')
        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            minCur, maxCur = float('Inf'), float('-Inf')
            for i in range(len(arr1)):
                minCur = min(minCur, arr1[i] * dx + arr2[i] * dy + i)
                maxCur = max(maxCur, arr1[i] * dx + arr2[i] * dy + i)
            ans = max(ans, maxCur - minCur)
        return ans
