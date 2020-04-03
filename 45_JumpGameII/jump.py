# 贪心： 每次跳到下一次能够跳的最远的点
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        nextStartIdx = 0
        furthestIdx = 0
        for i in range(len(nums) - 1):
            furthestIdx = max(furthestIdx, nums[i] + i)
            if i == nextStartIdx:
                nextStartIdx = furthestIdx
                steps += 1
        return steps
