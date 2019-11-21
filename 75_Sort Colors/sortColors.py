class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_0, right_2 = -1, len(nums)
        for i in range(right_2):
            while (nums[i] == 0 or nums[i] == 2) and left_0 < i and i < right_2:
                if nums[i] == 0:
                    left_0 += 1
                    nums[i], nums[left_0] = nums[left_0], nums[i]
                if nums[i] == 2:
                    right_2 -= 1
                    nums[i], nums[right_2] = nums[right_2], nums[i]
