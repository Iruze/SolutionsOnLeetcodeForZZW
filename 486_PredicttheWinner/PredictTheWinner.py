class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # # solution1
        # """
        # 如果数组长度为偶数，先手必胜， 因为：
        # 数组中，偶数位置的数的和 >=(或<=) 奇数位置的数的和，
        # 而先手可以提前瞄一下，计算这两个部分的和孰大孰小，然后决定拿哪一个部分（逼迫另个玩家拿另一部分）
        # 故，若数组长度为偶数，先手必胜
        # """
        # n = len(nums)
        # if n & 1 == 0:
        #     return True

        
        # dp = [[0 for _ in range(n)] for _ in range(n)]     # dp[i][j]表示在[i, j]范围内的分差
        # for i, num in enumerate(nums):
        #     dp[i][i] = num                                 # 此时只有一个数nums[i]，谁得计入谁的分（差）
        
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n):                      # i <= j，故正方形不超过反对角线的右半部分扫描
        #         dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        # return dp[0][n - 1] >= 0


        # solution2
        import functools

        @functools.lru_cache(None)
        def helper(l, r):
            if l == r:
                return nums[l]
            owe_l = nums[l] - helper(l + 1, r)    # pick左端，选手在此次子问题中比对手多得的分（差值）
            owe_r = nums[r] - helper(l, r - 1)    # pick右端
            return max(owe_l, owe_r)              # 希望比对手得的分更多，即分差越大越好
        
        return helper(0, len(nums) - 1) >= 0      # 若最终先手比后手分差不为负， 先手胜
