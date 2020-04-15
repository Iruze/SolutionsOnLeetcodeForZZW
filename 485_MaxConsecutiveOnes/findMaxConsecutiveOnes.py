# 方法一：双指针
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        lo = 0
        ans = 0
        for hi in range(len(nums)):
            if nums[hi] == 0:
                lo = hi
            else:
                if nums[lo] == 0:
                    lo = hi
                ans = max(ans, hi - lo + 1)
        return ans
        
        
# 方法二：利用python中的map和join函数
"""
- 在 Python 中可以使用 map 和 join 来解决此问题。
- 使用 splits 函数在 0 处分割将数组转换成字符串。
- 在获取子串的最大长度就是最大连续 1 的长度。
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split('0')))
