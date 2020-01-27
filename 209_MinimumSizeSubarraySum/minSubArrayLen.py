# solution1: 滑动窗口 -时间复杂度：O(N)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        cur = 0
        res = float('Inf')
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= s:
                res = min(res, right - left + 1)
                cur -= nums[left]
                left += 1
        return res if res != float('Inf') else 0
        
        
        
