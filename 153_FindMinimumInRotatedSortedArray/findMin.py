# 解法一： 二分法-我的解法
# 执行用时 :32 ms, 在所有 Python3 提交中击败了 98.51% 的用户
# 内存消耗 : 13.2 MB, 在所有 Python3 提交中击败了 44.85% 的用户
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if left == right or nums[left] < nums[right]:
            return nums[left]
        while left < right:
            if right - left == 1:
                return min(nums[left], nums[right])
            mid = (left + right) // 2
            if nums[left] < nums[mid] and nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        
        
# 解法二：选用 nums[right] < nums[mid], 不用nums[left]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 之所以不用nums[left] < nums[mid]
            # 是因为，对于[2, 1]这样的会停在2，故用right不用left
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
