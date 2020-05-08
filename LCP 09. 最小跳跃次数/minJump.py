class Solution:
    def minJump(self, jump: List[int]) -> int:
        n = len(jump)
        dp = [0 for _ in range(n)]
        # 自底向上
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            if jump[i] + i >= n:
                dp[i] = 1
            else:
                dp[i] = dp[i + jump[i]] + 1
            # j可以往左跳到i，dp[i]的变动可能会影响到dp[j]
            # dp[j] = min(dp[j], dp[i] + 1)， 因为剪枝，所以需要break
            for j in range(i + 1, n):
                if dp[j] < dp[i] + 1:
                    break
                dp[j] = dp[i] + 1
        return dp[0]
