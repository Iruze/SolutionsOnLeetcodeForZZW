class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0 : -1}
        res = 0
        # 将0，1数目相等转化为求和为k=0的最长连续子数组
        # 思路同 #325. 和等于k的最长子数组长度
        for idx, val in enumerate(nums):
            if val == 0:
                nums[idx] = -1
        cur = 0
        for idx, val in enumerate(nums):
            # 记录前缀和
            cur += val
            if cur in lookup:
                res = max(res, idx - lookup[cur])
            else:
                lookup[cur] = idx
        return res
