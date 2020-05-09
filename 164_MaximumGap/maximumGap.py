""" 桶排序
参考：
https://leetcode-cn.com/problems/maximum-gap/solution/tong-pai-xu-by-powcai/
"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        min_num, max_num = min(nums), max(nums)
        gap = math.ceil((max_num - min_num) / (n - 1))
        # 比如[1, 2, 3, 4，6]去掉了1, 6，只有[2, 3, 4]，划分 n - 1 个桶，有多余
        bucket = [[float('Inf'), float('-Inf')] for _ in range(n - 1)]

        # [2, 3, 4]入桶
        for num in nums:
            if num == min_num or num == max_num:
                continue
            lo = (num - min_num) // gap
            bucket[lo][0] = min(bucket[lo][0], num)
            bucket[lo][1] = max(bucket[lo][1], num)
        
        # 最大相邻差值在桶之间产生
        premin = min_num
        ans = float('-Inf')
        for x, y in bucket:
            # 前面的桶是最小值，min_num并没有入桶，要单独处理
            if x == float('Inf'):
                continue
            ans = max(ans, x - premin)
            premin = y
        # max_num也没有入桶，单独处理
        ans = max(ans, max_num - premin)

        return ans
