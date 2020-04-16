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
