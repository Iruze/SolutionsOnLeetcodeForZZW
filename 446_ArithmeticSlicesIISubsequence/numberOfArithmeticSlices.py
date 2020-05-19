from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(A))]
        ans = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] += dp[j][diff] + 1
                ans += dp[j][diff]
        return ans
        
