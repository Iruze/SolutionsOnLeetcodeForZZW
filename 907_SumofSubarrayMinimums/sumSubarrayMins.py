"""
单调栈思想：
参考：
https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-python3-by-smoon1989/
"""

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [float('-Inf')] + A + [float('-Inf')]
        ans = 0
        stack = []
        for i, v in enumerate(A):
            while stack and A[stack[-1]] > v:
                cur = stack.pop()
                ans += (i - cur) * (cur - stack[-1]) * A[cur]
            stack.append(i)
        return ans % (10 ** 9 + 7
