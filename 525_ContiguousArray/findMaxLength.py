class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        lookup = {0 : -1}
        ans = 0
        SUM = 0
        # 将0，1数目相等转化为求和为k=0的最长连续子数组
        # 思路同 #325. 和等于k的最长子数组长度
        for i, num in enumerate(nums):
            # 建模为： 0则-1， 1则+1， ”区间和“为0的时候则0和1数量相等
            SUM += 2 * num - 1
            if SUM in lookup:
                ans = max(ans, i - lookup[SUM])
            else:
                lookup[SUM] = i
        return ans     
