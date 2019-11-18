class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        front = len(nums) - 2
        while nums[front] >= nums[front + 1] and front >= 0:
            front -= 1
        if front >= 0:
            end = len(nums) - 1
            while nums[end] <= nums[front] and end > front:
                end -= 1
            nums[front], nums[end] = nums[end], nums[front]
        nums[front+1:] = nums[front+1:][::-1]
