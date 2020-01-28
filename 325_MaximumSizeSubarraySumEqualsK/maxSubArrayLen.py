class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        lookup = {0:-1}
        res = 0
        cur = 0
        for idx, val in enumerate(nums):
            cur += val
            if cur - k in lookup:
                res = max(res, idx - lookup[cur - k])
            # 如果存在idx，则维持最远的idx
            if cur not in lookup:
                lookup[cur] = idx
        return res
