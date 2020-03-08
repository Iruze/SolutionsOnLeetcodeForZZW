# 1. 如果nums的总和为奇数，则不可能分为两个和相等的子数组
# 2. 如果nums的总和为偶数，则等价于：从nums中选出如果个子数组，使得其总和等于 SUM/2
#    这时，等价于 0-1 背包问题。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        SUM = sum(nums)
        # 如果nums的总和为奇数，则不可分，返回False
        if SUM & 1:
            return False
        # 套用 0-1 背包问题：从nums中选择若干元素，使得它们构成的子数组总和等于 SUM/2
        SUM = SUM // 2
        res = [False] * (SUM + 1)
        # dp的base case
        res[0] = True
        # 1. 离散的选择作为外循环
        for num in nums:
            # 2. 0-1 背包是内循环反向迭代
            for j in range(SUM, num - 1, -1):
                res[j] = res[j] or res[j - num]
        return res[SUM]
