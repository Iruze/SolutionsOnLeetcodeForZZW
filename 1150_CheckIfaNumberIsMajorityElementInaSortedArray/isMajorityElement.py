# 二分法
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        lo = bisect.bisect_left(nums, target)
        if lo == n or nums[lo] != target:
            return False
        hi = bisect.bisect_right(nums, target)
        return hi - lo > n / 2
