# 典型的滑动窗口解题， 注意使用 滑动窗口模板： 
# https://github.com/Iruze/SolutionsOnLeetcodeForZZW/blob/master/SolutionsSummary/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%A8%A1%E6%9D%BF.md
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ds, dp = [0] * 26, [0] * 26
        # 提前统计好p中的字符
        for c in p:
            dp[ord(c) - ord('a')] += 1

        ls, lp = len(s), len(p)
        lo, hi = 0, 0
        ans = []
        while hi < ls:
            ds[ord(s[hi]) - ord('a')] += 1
            # 超出窗口，则出窗
            while hi - lo + 1 > lp:
                ds[ord(s[lo]) - ord('a')] -= 1
                lo += 1
            # 满足异位词
            if hi - lo + 1 == lp and ds == dp:
                ans.append(lo)
            hi += 1
        return ans
