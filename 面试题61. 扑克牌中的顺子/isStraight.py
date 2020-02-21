class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        zero = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                zero += 1
                continue
            if nums[i] == nums[i + 1]:
                return False
            if nums[i] + 1 < nums[i + 1]:
                zero -= nums[i + 1] - nums[i] - 1
        return zero >= 0
