"""
1. 所求的最大子数组和在 [max(nums), sum(nums)] 之内， 
2. 设置二分搜索的其实区间[lo, hi]为上述区间，统计 子数组和不超过 mid = (hi + lo) / 2 的个数
3. 如果 子数组和 不超过mid的个数 小于m，说明划分的子数组不够，设置的mid门限过小， lo = mid + 1;
   反之， 说明划分的子数组个数超出，设置的mid门限过大，hi = mid
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo = max(nums)
        hi = sum(nums)
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            total = 0
            cnt = 1
            for num in nums:
                total += num
                # 统计子数组和小于等于mid的子数组个数
                if total > mid:
                    cnt += 1
                    # 此时的子数组和为total - num， 
                    # 所以下一个子数组和从当前的num计
                    total = num
            # 说明子数组门限mid设置的过小
            if cnt > m:
                lo = mid + 1
            # 门限过大
            else:
                hi = mid
        return lo
