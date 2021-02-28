"""
python3 动态规划 + 回溯

先借用上一题 <139. 单词拆分> 来判断当前给定的s和wordDict是否是有效的拆分；
如果是有效的拆分，则用回溯法求不同的拆分结果
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # list转化为set, 加快查询
        wordSet = set(wordDict)

        @functools.lru_cache(None)
        def constructed(s):
            if not s: return True
            included = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordSet:
                    included |= constructed(s[i:])
            return included
            # n = len(s)
            # dp = [False] * (n + 1)
            # dp[0] = True
            # for i in range(1, n + 1):
            #     for j in range(i):
            #         if dp[j] and s[j:i] in wordDict:
            #             dp[i] = True
            #             break 
            # return dp[-1]

        # 回溯递归搜索s的构成方式
        def backtrace(s, pre=''):
            # 回溯递归终止条件
            if not s:
                ans.append(pre[:])
            for i in range(1, len(s) + 1):
                if s[:i] in wordSet:
                    cur = pre + ' ' + s[:i] if pre else s[:i]
                    backtrace(s[i:], cur)
        
        ans = []
        # 先判断s是否可以由wordDict构成
        if constructed(s):
            backtrace(s)
        return ans
