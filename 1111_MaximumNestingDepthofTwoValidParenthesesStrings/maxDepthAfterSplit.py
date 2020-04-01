class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = [0 for _ in range(len(seq))]
        idx = 0
        for s0 in seq:
            ans[idx] = idx & 1 if s0 == '(' else (idx + 1) & 1
            idx += 1
        return ans
