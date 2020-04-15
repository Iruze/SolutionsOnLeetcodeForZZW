class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans, count = 0, 0
        lo = 0
        # 维护[lo, hi]区间，区间最多K个0
        for hi in range(len(A)):
            if A[hi] == 0:
                count += 1
                # 区间多于K个0， lo右移，直至不大于K个0
                while count > K:
                    if A[lo] == 0:
                        count -= 1
                    lo += 1
            ans = max(ans, hi - lo + 1)
        return ans
