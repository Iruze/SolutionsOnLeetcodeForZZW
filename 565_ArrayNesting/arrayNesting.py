class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            count = 0
            start = i
            while nums[start] != 20001:
                count += 1
                nums[start], start = 20001, nums[start]
            res = max(res, count)
        return res
