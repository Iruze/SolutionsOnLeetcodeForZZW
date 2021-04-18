class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # list转化为set, 加快查询
        wordSet = set(wordDict)
        n = len(s)
        # # 解法一: 标准的dp
        # dp = [False] * (n + 1)
        # dp[0] = True
        # for i in range(1, n + 1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in wordSet:
        #             dp[i] = True
        #             break
        # return dp[-1]

        # 解法二: dp

        @functools.lru_cache(None)
        def dfs(s):
            if not s: return True
            for i in range(1, len(s) + 1):
                if s[:i] in wordSet and dfs(s[i:]):
                    return True
            return False
        
        wordSet = set(wordDict)
        return dfs(s)
