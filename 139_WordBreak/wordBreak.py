class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        if not s:
            return True
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        # dp里面的dp[i]表示基1的第i个元素
        for i in range(1, n + 1):
            for j in range(i):
                # s[j:i]是基0的，相当于基1的第j+1个元素开始
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break 
        return dp[-1]
