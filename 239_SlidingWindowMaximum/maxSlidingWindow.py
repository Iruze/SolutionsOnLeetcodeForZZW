class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, window = [], []
        # 单调栈解法，windon 维持递减值的索引，windon[0]记录最大值的索引
        for i in range(len(nums)):
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if i - k == window[0]:
                window.pop(0)
            if i - k >= -1:
                res.append(nums[window[0]])
        return res
