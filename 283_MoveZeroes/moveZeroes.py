# 快排思想

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = -1, 0
        for right, num in enumerate(nums):
            if num != 0:
                left += 1
                if left != right:
                    nums[left], nums[right] = nums[right], nums[left]
        
