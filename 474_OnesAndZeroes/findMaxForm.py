# python3二维dp, 0-1背包只有一个背包容量，本题则是两个背包重量，换汤不换药，模板伺候
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 备选物件在外循环
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = s.count('1')
            # 连续的背包重量在内循环
            # 0-1背包是逆序遍历，且到当前物件重量止，而完全背包则为正序
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        return dp[-1][-1]
