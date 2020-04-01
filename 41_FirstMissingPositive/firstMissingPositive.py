class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1
    
    def __swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
