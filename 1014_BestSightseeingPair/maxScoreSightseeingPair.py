"""
思路：
已知题目要求 res = A[i] + A[j] + i - j （i < j） 的最大值，
而对于输入中的每一个 A[j] 来说， 它的值 A[j] 和它的下标 j 都是固定的，
所以 A[j] - j 的值也是固定的。
因此，对于每个 A[j] 而言， 想要求 res 的最大值，也就是要求 A[i] + i （i < j） 的最大值，
所以不妨用一个变量 pre_max 记录当前元素 A[j] 之前的 A[i] + i 的最大值，
这样对于每个 A[j] 来说，都有 最大得分 = pre_max + A[j] - j，
再从所有 A[j] 的最大得分里挑出最大值返回即可。
"""
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = 0
        premax = A[0]
        for i in range(1, len(A)):
            premax = max(premax, A[i - 1] + i - 1)
            res = max(res, premax + A[i] - i)
        return res
