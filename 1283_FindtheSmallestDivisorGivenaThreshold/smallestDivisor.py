"""python3, 

同类型的题目，几乎一模一样：

- [875. 爱吃香蕉的珂珂](https://leetcode-cn.com/problems/koko-eating-bananas/)

典型的二分法，模板一把唆：
"""
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math

        lo = 1
        hi = math.ceil(max(nums) * len(nums) / threshold)
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            res = sum(math.ceil(nums[i] / mid) for i in range(len(nums)))
            if res > threshold:
                lo = mid + 1
            else:
                hi = mid
        return lo
