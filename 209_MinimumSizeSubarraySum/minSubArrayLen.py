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
        
        
# solution2: 二分查找（前缀和）
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        if nums[-1] < s:
            return 0
        res = float('Inf')
        nums = [0] + nums
        for i in range(len(nums)):
            if nums[i] >= s:
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                else:
                    res = min(res, i - loc + 1)
        return res
