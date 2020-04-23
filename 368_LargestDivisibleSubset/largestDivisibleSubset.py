class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # dp[i] 表示 nums[i] 的约数集合
        dp = [[x] for x in nums]
        ans = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(ans):
                ans = dp[i]
        return ans
