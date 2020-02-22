# 解法一：
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def _backtrack(first=0):
            if first == len(nums):
                output.append(nums[:])
            for i in range(first, len(nums)):
                if nums[i] not in nums[first:i]:
                    nums[i], nums[first] = nums[first], nums[i]
                    _backtrack(first + 1)
                    nums[i], nums[first] = nums[first], nums[i]
        output = []
        _backtrack()
        return output


# 解法二：
