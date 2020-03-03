# 解法一：借用bisect模块
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        left = bisect.bisect_left(nums, target)
        # 如果插入的数在头或者尾，且不在数组中，则无效
        if left == 0 and nums[0] != target or left == len(nums) and nums[-1] != target:
            return [-1, -1]
        # left = right，证明数组中不含target，则无效
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        # right实际是target右边位置的后一个数
        return [left, right - 1]

# 解法二：标准的二分查找
