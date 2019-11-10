class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                self.__swap(nums, i, nums[i] - 1)
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                output.append(nums[i])
        return output
    
    def __swap(self, nums, idx1, idx2):
        if nums[idx1] == nums[idx2]: return
        nums[idx1] = nums[idx1] ^ nums[idx2]
        nums[idx2] = nums[idx1] ^ nums[idx2]
        nums[idx1] = nums[idx1] ^ nums[idx2]
