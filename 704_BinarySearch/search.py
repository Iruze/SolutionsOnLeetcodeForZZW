class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or nums[-1] < target:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1
