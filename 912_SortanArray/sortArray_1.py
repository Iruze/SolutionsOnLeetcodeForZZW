import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        self.__quickSort(nums, 0, len(nums) - 1)
        return nums
    
    
    def __partition(self, nums, start, end):
        index = random.randint(start, end)
        nums[index], nums[end] = nums[end], nums[index]
        small = start - 1
        for i in range(start, end):
            if nums[i] < nums[end]:
                small += 1
                if small != i:
                    nums[i], nums[small] = nums[small], nums[i]
        small += 1
        nums[small], nums[end] = nums[end], nums[small]
        return small
    
    
    def __quickSort(self, nums, start, end):
        if start >= end:
            return
        index = self.__partition(nums, start, end)
        if start < index:
            self.__quickSort(nums, start, index - 1)
        if index < end:
            self.__quickSort(nums, index + 1, end)
