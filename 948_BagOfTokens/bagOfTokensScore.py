"""
先对数组排序，使用双指针，left，right。
根据贪心策略，
令牌正面朝上，我们需要尽可能失去少的能量，从左往右，left++
令牌反面朝上，我们需要尽可能多得到能量，从右往左，right--
每次维护最大的得分即可。
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        lo, hi = 0, len(tokens) - 1
        ans = 0
        score = 0
        tokens.sort()
        while lo <= hi:
            if P >= tokens[lo]:
                P -= tokens[lo]
                lo += 1
                score += 1
            else:
                if score <= 0:
                    return ans
                P += tokens[hi]
                hi -= 1
                score -= 1
            ans = max(ans, score)
        return ans
