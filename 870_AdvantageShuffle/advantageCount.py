""" 田忌赛马贪心策略
1. A当前最小值如果比B的当前最小值要大，让这两个最小值配对
2. 否则， A当前最小值和当前最大值配对，让每一个A中的值都发挥最大效用
"""
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        B_idx = sorted([*zip(range(n), B)], key=lambda x:x[1])
        A.sort()
        ans = [0 for _ in range(n)]
        min_pos, max_pos = 0, n - 1
        for i, v in enumerate(A):
            if v > B_idx[min_pos][1]:
                ans[B_idx[min_pos][0]] = v
                min_pos += 1
            else:
                ans[B_idx[max_pos][0]] = v
                max_pos -= 1
        return ans
