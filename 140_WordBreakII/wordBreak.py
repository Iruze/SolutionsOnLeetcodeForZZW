"""
python3 动态规划 + 回溯

先借用上一题 <139. 单词拆分> 来判断当前给定的s和wordDict是否是有效的拆分；
如果是有效的拆分，则用回溯法求不同的拆分结果
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        output = []
        # 1. 判断wordDict中的单词是否可以构建s
        def constructed():
            if not wordDict:
                return False
            if not s:
                return True
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

        # 2. 回溯求分解结果
        def backtrack(cur, s):
            if not s:
                output.append(cur.strip(' ')[:])
                return
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    cur += s[:i] + ' '
                    backtrack(cur, s[i:])
                    cur = cur.strip()[:-i]

        # 只有由wordDict可以构建s才用 backtrack() 回溯求分解结果
        if constructed():
            backtrack('', s)
        return output
