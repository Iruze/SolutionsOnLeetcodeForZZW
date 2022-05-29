class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 标准的二分法解法，注意right=len(nums)
        # 包含了target > nums[-1]的用例
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
