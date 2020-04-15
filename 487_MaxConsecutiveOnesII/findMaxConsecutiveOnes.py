"""
只用维护一个区间，这个区间中最多只包含一个0。
当区间中包含两个0的时候，直接移动左边界l直到区间只包含一个0即可。
这个过程中去更新最大区间长度，最后就能得到答案。
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans, count = 0, 0
        lo = 0
        for hi in range(len(nums)):
            if nums[hi] == 0:
                count += 1
                while count > 1:
                    if nums[lo] == 0:
                        count -= 1
                    lo += 1
            ans = max(ans, hi - lo + 1)
        return ans
