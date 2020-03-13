# 二分法
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        lo = bisect.bisect_left(nums, target)
        # 如果target不存在nums：插入到nums的尾部，或者首部0
        if lo == n or nums[lo] != target:
            return False
        # 如果lo存在，则hi必然存在
        hi = bisect.bisect_right(nums, target)
        return hi - lo > n / 2
