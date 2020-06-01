class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = dict()
        for a in arr:
            dp[a] = (dp[a - difference] if a - difference in dp else 0) + 1
        return max(dp.values())       
