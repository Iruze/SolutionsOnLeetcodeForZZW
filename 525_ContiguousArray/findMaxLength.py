class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0 : -1}
        ans = 0
        SUM = 0
        # 将0，1数目相等转化为求和为k=0的最长连续子数组
        # 思路同 #325. 和等于k的最长子数组长度
        for i, num in enumerate(nums):
            SUM += 2 * num - 1
            if SUM in lookup:
                ans = max(ans, i - lookup[SUM])
            else:
                lookup[SUM] = i
        return ans     
