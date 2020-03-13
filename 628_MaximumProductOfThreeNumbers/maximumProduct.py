class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # 当num[0], num[1]为负数的时候
        if nums[0] * nums[1] > nums[-2] * nums[-3]:
            return nums[0] * nums[1] * nums[-1]
        else:
            return nums[-3] * nums[-2] * nums[-1]
