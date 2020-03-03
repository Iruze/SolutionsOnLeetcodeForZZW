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
# 实质是用_posLR()函数替代bisect.bisect_left()和bisect.bisect_right()函数
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        left = self._posLR(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = self._posLR(nums, target, False)
        # right实际是target右边位置的后一个数
        return [left, right - 1]
    
    def _posLR(self, nums, target, isLeft):
        # 注意： right = len(nums)
        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            # 1. target < nums[mid]
            # 2. 左寻找，且target == nums[mid]，此时当做target < nums[mid]，
            #    这样才能向left左边靠拢
            if target < nums[mid] or isLeft and target == nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
