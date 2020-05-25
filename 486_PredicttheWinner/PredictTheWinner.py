class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        如果数组长度为偶数，先手必胜， 因为：
        数组中，偶数位置的数的和 >=(或<=) 奇数位置的数的和，
        而先手可以提前瞄一下，计算这两个部分的和孰大孰小，然后决定拿哪一个部分（逼迫另个玩家拿另一部分）
        故，若数组长度为偶数，先手必胜
        """
        n = len(nums)
        if n & 1 == 0:
            return True

        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i, num in enumerate(nums):
            dp[i][i] = num
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        return dp[0][n - 1] >= 0
