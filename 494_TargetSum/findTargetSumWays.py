class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 典型01背包问题：nums中找到若干个数，使得总和为SUM
        def helper(nums, SUM):
            dp = [0] * (SUM + 1)
            dp[0] = 1
            for num in nums:
                for i in range(SUM, num - 1, -1):
                    dp[i] += dp[i - num]
            return dp[-1]
        """ 
        原题等价于：在nums中找到正数子集P， 和负数子集N，使得:
        P - N = S
        从而，P + N + P - N = P + N + S
        所以， P = (S + SUM) // 2
        进而，转化为01背包问题：从nums中找到正数子集P
        """
        SUM = sum(nums)
        if S > SUM or S < -SUM or (S + SUM) & 1:
            return 0
        return helper(nums, (SUM + S) >> 1)
